from django.shortcuts import render, redirect
from django.db.models import Max, Min
from . models import *
from users.models import Profile

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
        for node in nodes:
            thread = Thread.objects.filter(node=node, is_visible=True).order_by('-time_created')
            if thread:
                last_threads.append(thread[0])

        context = {
            'tree':tree,
            'threads':threads,
            'last_threads': last_threads
        }
        # print(tree)
    return render(request, "forum_main.html", context)

def build_nodes_tree(nodes, parent=None):
    tree = []
    for node in nodes:
        if node.parent == parent:
            children = build_nodes_tree(nodes, parent=node)
            tree.append({'node': node, 'children': children})
    return tree