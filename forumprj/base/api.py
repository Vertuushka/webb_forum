from django.http import JsonResponse
from django.contrib.auth.decorators import permission_required
from django.core.serializers import serialize
from users.models import Warnings_history
from forum.models import Message

@permission_required("users.view_warnings_history", raise_exception=False)
def get_warning_by_message(request, msg_id):
    data = {}
    try:
        message = Message.objects.get(id=msg_id)
        warning = Warnings_history.objects.get(forum_msg=message)
    except:
        data['error'] = "doesn't exists"
    else:
        if warning.user:
            user_data = {
                'id': warning.user.id,
                'username': warning.user.username,
                'profile_picture': warning.user.profile.profile_picture
            }
            data['user'] = user_data
        if warning.forum_msg:
            forum_msg_data = {
                'id': warning.forum_msg.id,
                'author_id': warning.forum_msg.user.id,
                'author_username': warning.forum_msg.user.username,
                'author_profile_pictire': warning.forum_msg.user.profile.profile_picture,
                'node_name': warning.forum_msg.thread.node.name,
                'node_slug': warning.forum_msg.thread.node.slug,
                'thread_id': warning.forum_msg.thread.id,
                'thread_title': warning.forum_msg.thread.title,
                'thread_slug': warning.forum_msg.thread.slug,
                'thread_is_visible': warning.forum_msg.thread.is_visible,
                'message': warning.forum_msg.message,
            }
            data['message'] = forum_msg_data
        if warning.warned_by:
            warner_data = {
                'id': warning.warned_by.id,
                'username': warning.warned_by.username,
                'profile_picture': warning.warned_by.profile.profile_picture
            }
            data['warned_by'] = warner_data
        if warning.details:
            data['details'] = warning.details
        if warning.time_warned:
            data['time_warned'] = warning.time_warned.strftime("%d/%m/%Y - %H:%M")

    return JsonResponse(data)