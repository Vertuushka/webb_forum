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
    node = Node.objects.get(name = section)
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

def thread(request, section, thread):
    try:
        _section = Node.objects.get(name=section)
        _thread = Thread.objects.get(title=thread, node=_section)
    except:
        try:
            _thread = Thread.objects.get(title=thread)
        except:
            return redirect('error_page')
        else:
            return redirect('thread', _thread.node.name, _thread.title)
    else:
        msgs = Message.objects.filter(thread=_thread).order_by('time_created')
        print(msgs)
        context = {
            'thread':_thread,
            'messages': msgs
        }
        return render(request, 'forum_thread.html', context)