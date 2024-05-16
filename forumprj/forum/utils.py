from datetime import datetime

def build_nodes_tree(nodes, parent=None):
    tree = []
    for node in nodes:
        if node.parent == parent:
            children = build_nodes_tree(nodes, parent=node)
            tree.append({'node': node, 'children': children})
    return tree

def get_reason_input(request):
    notification = None
    reason = request.POST.get('reason')
    if request.POST.get('is_notified'):
        notification = request.POST.get('notification')
    return {'reason': reason, 'notification':notification}

def delete_thread(request, thread, reason):
    thread.is_visible = False
    thread.invis_reason = reason
    thread.deleted_by = request.user
    thread.save()
    return True

def delete_message(request, message, reason):
    if message.is_start:
        deleting_thread = delete_thread(request, message.thread, reason)
        if not deleting_thread:
            return False
    message.thread.msg_amount -= 1
    message.thread.save()
    
    message.is_visible = False
    message.deleted_by = request.user
    message.invis_reason = reason
    message.save()
    return True