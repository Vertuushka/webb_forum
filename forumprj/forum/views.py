from django.utils.text import slugify
from django.shortcuts import render, redirect
from django.db.models import Max, Min, Count
from . models import *
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
    section = section.replace('-', ' ')
    # print(section)
    node = Node.objects.get(name__iexact = section)
    threads_in_node = Thread.objects.filter(node=node)
    threads = []
    for thread in threads_in_node:
        last_msg = Message.objects.filter(thread=thread, is_visible=True).order_by('-time_created').first()
        if last_msg:
            threads.append((thread, last_msg))
    context = {
        "node": node,
        "threads": threads
    }
    return render(request, "forum_section.html", context)

def thread(request, section, thread, thread_id):
    section = section.replace('-', ' ')
    thread = thread.replace('-', ' ')
    _thread = Thread.objects.get(id=thread_id)
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