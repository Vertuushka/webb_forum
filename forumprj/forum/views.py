from django.shortcuts import render, redirect
from django.db.models import Max, Min
from . models import *
from users.models import Profile

def forum_main(request):
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