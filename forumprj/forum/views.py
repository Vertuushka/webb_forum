from django.shortcuts import render, redirect
from . models import *

def forum_main(request):
    nodes = Node.objects.all()
    tree = build_nodes_tree(nodes)
    context = {
        'tree':tree
    }
    return render(request, "forum_main.html", context)

def build_nodes_tree(nodes, parent=None):
    tree = []
    for node in nodes:
        if node.parent == parent:
            children = build_nodes_tree(nodes, parent=node)
            tree.append({'node': node, 'children': children})
    return tree