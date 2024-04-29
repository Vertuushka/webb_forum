from django.utils.text import slugify
from django.shortcuts import render, redirect
from django.db.models import Max, Min, Count
from . models import *
from datetime import datetime
# from users.models import Profile

def forum_main(request):
    context = {}
    if request.method == "POST":
        context['forum_search'] = True
        content_type = request.POST.get("content_type")
        searched = request.POST.get("search")
        if content_type:
            if content_type == "threads":
                results = Thread.objects.filter(title__icontains=searched)
            if content_type == "members":
                results = User.objects.filter(username__icontains=searched)
        else:
            results = Message.objects.filter(content__icontains=searched)
        context['results'] = results
    else:
        nodes = Node.objects.all()
        tree = build_nodes_tree(nodes)
        last_threads = []
        for node in nodes:
            threads = Thread.objects.filter(node=node, is_visible=True).annotate(
            latest_msg_time=Max('message__time_created')).order_by('-latest_msg_time')[:3]
            last_threads.extend(threads)
        context = {
            'tree':tree,
            'threads':threads,
            'last_threads': last_threads
        }
    return render(request, "forum_main.html", context)

def build_nodes_tree(nodes, parent=None):
    tree = []
    for node in nodes:
        if node.parent == parent:
            children = build_nodes_tree(nodes, parent=node)
            tree.append({'node': node, 'children': children})
    return tree

def section(request, section):
    context = {}
    section = section.replace('-', ' ')
    try:
        node = Node.objects.get(name__iexact = section)
    except: 
        return render(request, 'error.html')
    try:
        child_nodes = Node.objects.filter(parent=node)
        context["child_nodes"] = child_nodes
    except:
        context["child_nodes"] = False
    threads_in_node = Thread.objects.filter(node=node)
    threads = []
    for thread in threads_in_node:
        last_msg = Message.objects.filter(thread=thread, is_visible=True).order_by('-time_created').first()
        if last_msg:
            threads.append((thread, last_msg))
    context ["node"] = node
    context ["threads"] = threads
    return render(request, "forum_section.html", context)

def thread(request, section, thread, thread_id):
    section = section.replace('-', ' ')
    thread = thread.replace('-', ' ')
    try:
        _thread = Thread.objects.get(id=thread_id)
    except: 
        return render(request, 'error.html')
    try: 
        _section = Node.objects.get(name__iexact=section)
        _magic = Thread.objects.get(title__iexact=thread)
    except:
        return redirect('thread', slugify(_thread.node.name), slugify(_thread.title), thread_id)
    else:
        if _thread.node != _section or not _magic:
            return redirect('thread', slugify(_thread.node.name), slugify(_thread.title), thread_id)

    msgs = Message.objects.filter(thread=_thread).order_by('time_created')
    # print(msgs)
    context = {
        'thread':_thread,
        'messages': msgs
    }
    return render(request, 'forum_thread.html', context)

def main_redirecter(request):
    return redirect('forum_main')

def create_thread(request, section, section_id):
    try:
        node = Node.objects.get(id=section_id)
        if (node.staff_only and not request.user.is_staff) or (not node.staff_only and not request.user.is_authenticated):
            return render(request, 'error.html')
    except:
        return render(request, 'error.html')
    if request.method == "POST":
        title = request.POST.get('title')
        text = request.POST.get('msg')
        author = request.user
        new_thread = Thread.objects.create(user=author, title=title, node=node)
        new_thread.save()
        first_message = Message.objects.create(thread=new_thread, user=author, message=text)
        first_message.save()
        return redirect('thread', slugify(new_thread.node.name), slugify(new_thread.title), new_thread.id)
    context = {
        'node':node
    }
    return render(request, 'new_thread.html', context)