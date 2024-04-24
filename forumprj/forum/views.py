from django.shortcuts import render, redirect
from django.db.models import Max, Min
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
                results = User.objects.filter(first_name__icontains=searched)
        else:
            results = Message.objects.filter(content__icontains=searched)
        context['results'] = results
    else:
        nodes = Node.objects.all()
        threads = Thread.objects.all()
        tree = build_nodes_tree(nodes)
        last_threads = []
        last_msgs_unsorted = []
        for node in nodes:
            threads_in_node = Thread.objects.filter(node=node, is_visible=True)
            if threads_in_node:
                for thread in threads_in_node:
                    msg = Message.objects.filter(thread=thread, is_visible=True).order_by('-time_created')[0]
                    last_msgs_unsorted.append(msg)
        last_msgs = sorted(last_msgs_unsorted, key=lambda x: x.time_created, reverse=True)
        for msg in last_msgs:
            last_threads.append(msg.thread)
        
        context = {
            'tree':tree,
            'threads':threads,
            'last_threads': zip(last_threads, last_msgs)
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
    last_msgs_unordered = []
    threads = []
    for thread in threads_in_node:
        msg = Message.objects.filter(thread=thread, is_visible=True).order_by('-time_created')[0]
        last_msgs_unordered.append(msg)
    last_msgs = sorted(last_msgs_unordered, key=lambda x: x.time_created, reverse=True)
    for msg in last_msgs:
        threads.append(msg.thread)
    context = {
        "node": node,
        "threads": zip(threads, last_msgs)
    }
    return render(request, "forum_section.html", context)
    