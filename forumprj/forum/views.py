from django.shortcuts import render, redirect
from django.db.models import Max
from django.contrib.auth.decorators import permission_required, login_required
from django.urls import reverse
from . models import *
from moderation.models import Report
from datetime import datetime
from base.utils import notify_user
from .utils import *
from users.models import Warnings_history
from base import base_strings

def forum_main(request):
    context = {}
    if request.method == "POST":
        context['forum_search'] = True
        content_type = request.POST.get("content_type")
        searched = request.POST.get("search")
        context['type'] = 'posts'
        if content_type:
            if content_type == "threads":
                results = Thread.objects.filter(title__icontains=searched)
                context['type'] = 'threads'
            if content_type == "members":
                results = User.objects.filter(username__icontains=searched)
                context['type'] = 'members'
        else:
            results = Message.objects.filter(message__icontains=searched)
        context['results'] = results
        
    else:
        nodes = Node.objects.all()
        tree = build_nodes_tree(nodes)
        last_threads = []
        for node in nodes:
            threads = Thread.objects.filter(node=node, is_visible=True).annotate(
            latest_msg=Max('message__id')).order_by('-latest_msg')[:3] # take and show only 3 threads, with time sorting
            last_threads.extend(threads)
        context = {
            'tree':tree,
            'threads':threads,
            'last_threads': last_threads
        }
    return render(request, "forum_main.html", context)


def section(request, section):
    context = {}
    try:
        node = Node.objects.get(slug__iexact = section)
    except: 
        return render(request, 'error.html', {'error_str':base_strings.ERRORS['node_not_found']})
    try:
        child_nodes = Node.objects.filter(parent=node)
        context["child_nodes"] = child_nodes
    except:
        context["child_nodes"] = False
    threads_in_node = Thread.objects.filter(node=node).annotate(
            latest_msg=Max('message__id')).order_by('-id')
    pinned_threads = []
    unpinned_threads = []
    for thread in threads_in_node:
        last_msg = Message.objects.filter(thread=thread).order_by('-id').first()
        if last_msg:
            # sorting threads by pinned or unpinned threads
            if last_msg.thread.is_pinned:
                pinned_threads.append((thread, last_msg))
            else:
                unpinned_threads.append((thread, last_msg))
    threads = pinned_threads + unpinned_threads
    context ["node"] = node
    context ["threads"] = threads
    # print(threads)
    return render(request, "forum_section.html", context)

def thread(request, section, thread, thread_id):
    try:
        _thread = Thread.objects.get(id=thread_id)
        if (not _thread.is_visible) and (not request.user.has_perm('forum.view_thread')):
            return render(request, 'error.html', {'error_str':base_strings.ERRORS['perms_required']})
        if (_thread.node.type_private and (request.user != _thread.user and not request.user.has_perm('forum.view_thread'))):
            return redirect('section', _thread.node.slug)
    except: 
        return render(request, 'error.html', {'error_str':base_strings.ERRORS['thread_not_found']})
    try: 
        _section = Node.objects.filter(slug__iexact=section)    
        _magic = Thread.objects.filter(slug__iexact=thread)
    except:
        # slugify rewriting text to slug
        return redirect('thread', _thread.node.slug, _thread.slug, thread_id)
    else:
        if _thread.node not in _section or not any(_magic):
            return redirect('thread', _thread.node.slug, _thread.slug, thread_id)
    # message inside Thread
    if request.method == "POST":
        new_message = request.POST.get('msg')
        message = Message.objects.create(thread = _thread, user=request.user, message=new_message)
        message.save()
        _thread.msg_amount += 1
        _thread.save()
        return redirect('msg_redirect', _thread.node.slug, _thread.slug, _thread.id, message.id)
    msgs_usual = list(Message.objects.filter(thread=_thread, is_solution=False).order_by('id'))
    try: # if there is a message marked as solution
        msg_solution = Message.objects.get(thread=_thread, is_solution=True)
        msgs_usual.insert(1, msg_solution)
    except: # if there is not solution - do nothing 
        pass       
    context = {
        'thread':_thread,
        'messages': msgs_usual
    }
    return render(request, 'forum_thread.html', context)

def main_redirecter(request):
    return redirect('forum_main')

@login_required()
def create_thread(request, section, section_id):
    try:
        node = Node.objects.get(id=section_id)
        if (node.staff_only and not request.user.is_staff) or (not node.staff_only and not request.user.is_authenticated):
            return render(request, 'error.html', {'error_str':base_strings.ERRORS['perms_required']})
    except:
        return render(request, 'error.html', {'error_str':base_strings.ERRORS['node_not_found']})
    if request.method == "POST":
        title = request.POST.get('title')
        text = request.POST.get('msg')
        author = request.user
        new_thread = Thread.objects.create(user=author, title=title, node=node)
        new_thread.save()
        first_message = Message.objects.create(thread=new_thread, user=author, message=text, is_start=True)
        first_message.save()
        return redirect('thread', new_thread.node.slug, new_thread.slug, new_thread.id)
    context = {
        'node':node
    }
    return render(request, 'new_thread.html', context)

def msg_redirect(request, section, thread, thread_id, msg_id):
    try:
        message = Message.objects.get(id=msg_id)
    except:
        return render(request, 'error.html', {'error_str':base_strings.ERRORS['msg_not_found']})
    if (not message.thread.is_visible) and (not request.user.has_perm('forum.view_thread')):
        return render(request, 'error.html', {'error_str':base_strings.ERRORS['perms_required']})
    if (message.thread.node.type_private and (request.user != message.thread.user and not request.user.has_perm('forum.view_thread'))):
        return redirect('section', message.thread.node.slug)
    url = reverse('thread', kwargs={'section': message.thread.node.slug, 'thread': message.thread.slug, 'thread_id': message.thread.id})
    anchor_url = f'{url}#{msg_id}'
    return redirect(anchor_url)

@login_required()
def report_msg(request, msg_id):
    try:
        msg = Message.objects.get(id=msg_id)
    except:
        return render(request, 'error.html', {'error_str':base_strings.ERRORS['msg_not_found']})
    if request.method == "POST":
        reason = request.POST.get('reason')
        new_report = Report.objects.create(
            content=msg, 
            user=request.user, 
            reason=reason)
        new_report.save()
        return redirect('thread', msg.thread.node.slug, msg.thread.slug, msg.thread.id)
    return render(request, 'error.html')

@permission_required('forum.change_thread', raise_exception=False)
def toggle_close_thread(request, thread_id):
    try:
        thread = Thread.objects.get(id=thread_id)
    except:
        return render(request, 'error.html', {'error_str':base_strings.ERRORS['thread_not_found']})
    thread.is_closed = False if thread.is_closed else True
    thread.save()   
    return redirect('thread', thread.node.slug, thread.slug, thread.id)

@permission_required('forum.change_thread', raise_exception=False)
def toggle_thread_visibility(request, thread_id):
    try:
        thread = Thread.objects.get(id=thread_id)
    except:
        return render(request, 'error.html', {'error_str':base_strings.ERRORS['thread_not_found']})
    if request.method == "POST":
        deleting_form = get_reason_input(request)
        delete_thread(request, thread, deleting_form["reason"])
        if deleting_form["notification"] != None:
            notify_user(
                user = thread.user, 
                notification_type = 'thread_delete',
                reason = thread,
                notification = deleting_form["notification"]
            )
        thread.save()
        return redirect('section', thread.node.slug)
    else:
        if not thread.is_visible:
            thread.is_visible = True
            thread.save()
        return redirect('thread', thread.node.slug, thread.slug, thread.id)

@permission_required('forum.change_thread', raise_exception=False)
def toggle_thread_pin(request, thread_id):
    try:
        thread = Thread.objects.get(id=thread_id)
    except:
        return render(request, 'error.html', {'error_str':base_strings.ERRORS['thread_not_found']})
    thread.is_pinned = False if thread.is_pinned else True
    thread.save()
    return redirect('thread', thread.node.slug, thread.slug, thread.id)

@permission_required('forum.change_message', raise_exception=False)
def toggle_msg_visibility(request, msg_id):
    try:
        message = Message.objects.get(id=msg_id)
    except:
        return render(request, 'error.html', {'error_str':base_strings.ERRORS['msg_not_found']})
    if request.method == "POST":
        deleting_form = get_reason_input(request)
        delete_message(request, message, deleting_form["reason"])
        if deleting_form["notification"] != None:
            notify_user(user=message.user,
                        notification_type='message_delete',
                        reason=message,
                        notification=deleting_form["notification"])
            if request.POST.get('notify_thread'):
                notify_user(user=message.user,
                            notification_type='thread_delete',
                            reason=message.thread,
                            notification=deleting_form["notification"])
        if message.is_start and not request.user.has_perm("forum.view_thread"):
            return redirect('section', message.thread.node.slug)
        else:
            return redirect('thread', message.thread.node.slug, message.thread.slug, message.thread.id)
    else:
        message.is_visible = True
        message.thread.msg_amount += 1
        message.thread.save()
        message.save()
        pass
    return redirect('thread', message.thread.node.slug, message.thread.slug, message.thread.id)

@permission_required('forum.change_message', raise_exception=False)
def change_message(request, msg_id):
    try:
        message = Message.objects.get(id=msg_id)
    except:
        return render(request, 'error.html')
    if request.method == "POST":
        new_msg = request.POST.get('new_msg')
        message.message = new_msg
        message.time_changed = datetime.now()
        message.changer = request.user
        if request.POST.get('is_notified') == "on":
            notify_user(user=message.user, 
                        notification_type="message_edit",
                        reason=message,
                        notification=request.POST.get('notification'))
        message.save()
    return redirect('thread', message.thread.node.slug, message.thread.slug, message.thread.id)

@permission_required('users.create_warnings_history', raise_exception=False)
def warn_user(request, msg_id):
    try:
        message = Message.objects.get(id=msg_id)
    except:
        return render(request, 'error.html', {'error_str':base_strings.ERRORS['msg_not_found']})
    if request.method == "POST":
        details = request.POST.get("warn_reason")
        warning = Warnings_history.objects.create(user=message.user, 
                                                  forum_msg=message,
                                                  warned_by=request.user,
                                                  details=details, 
                                                  time_warned=datetime.now())
        warning.save()
        message.user.profile.warnings += 1
        message.user.profile.save()
        notify_user(user=message.user,
                    notification_type="warning",
                    reason=warning,
                    notification=details)

        if request.POST.get("is_deleted")  == "on":
            reason = request.POST.get("deleting_reason")
            # print(reason)
            try_delete = delete_message(request, message, reason)
            if not try_delete:
                return render(request, 'error.html')
        if message.is_start:
            return redirect('section', message.thread.node.slug)
    return redirect('thread', message.thread.node.slug, message.thread.slug, message.thread.id)

@login_required
def mark_solution(request, msg_id):
    try:
        message = Message.objects.get(id=msg_id)
        if message.thread.user != request.user and not request.user.has_perm('forum.change_message'):
            return redirect('msg_redirect', message.thread.node.slug, message.thread.slug, message.thread.id, message.id)
    except:
        return render(request, 'error.html', {'error_str':base_strings.ERRORS['msg_not_found']})
    try:
        solution = Message.objects.get(thread=message.thread, is_solution=True)
        if solution != message:
            solution.is_solution = False
            solution.save()
    except:
        pass
    message.is_solution = False if message.is_solution else True
    message.save()
    return redirect('msg_redirect', message.thread.node.slug, message.thread.slug, message.thread.id, message.id)

@permission_required('forum.change_thread')
def change_thread(request, thread_id):
    try:
        thread = Thread.objects.get(id=thread_id)
    except:
        return render(request, 'error.html', {'error_str':base_strings.ERRORS['thread_not_found']})
    if request.method == "POST":
        new_thread_name = request.POST['title']
        thread.title = new_thread_name
        thread.save()
        if request.POST['is_notified'] == "on":
            notify_user(user=thread.user,
                        notification_type="thread_change",
                        reason=thread,
                        notification=request.POST['notification'])
    return redirect('thread', thread.node.slug, thread.slug, thread.id)
