from django.shortcuts import render, redirect
from .models import *
from forum.models import Message
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from base import base_strings
# Create your views here.
@login_required()
def bookmarks_main(request):
    user = request.user
    context = {}
    try:
        bookmarks = Bookmark.objects.filter(user=user).order_by('-id')
        context["bookmarks"] = bookmarks
    except:
        context["bookmarks"] = False
    return render(request, 'bookmarks.html', context)

@login_required()
def add_msg_bookmark(request, id):
    try:
        msg = Message.objects.get(id=id)
        if msg.thread.node.type_private and (request.user != msg.thread.user or not request.user.has_perm('forum.view_thread')):
            return redirect('section', msg.thread.node.slug)
    except:
        return render(request, 'error.html', {'error_str': base_strings.ERRORS['msg_not_found']})
    try:
        exists = Bookmark.objects.get(user=request.user, forum_msg=msg)
        return redirect('msg_redirect', msg.thread.node.slug, msg.thread.slug, msg.thread.id, msg.id)
    except:
        bookmark = Bookmark.objects.create(user=request.user, forum_msg=msg)
        bookmark.save()
    # url = reverse('msg_redirect', args=(msg.thread.node.slug, msg.thread.slug, msg.thread.id, msg.id))
    # print(url)
    # return redirect(url)
    return redirect('msg_redirect', msg.thread.node.slug, msg.thread.slug, msg.thread.id, msg.id)

@login_required()
def del_bookmark(request, id):
    try:
        bookmark = Bookmark.objects.get(user=request.user, id=id).delete()
    except:
        pass
    return redirect('bookmarks_main')
    