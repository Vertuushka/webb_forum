from django.shortcuts import render, redirect
from .models import *
from forum.models import Message
from django.utils.text import slugify
from django.urls import reverse

# Create your views here.
def bookmarks_main(request):
    user = request.user
    context = {}
    try:
        bookmarks = Bookmark.objects.filter(user=user)
        context["bookmarks"] = bookmarks
    except:
        context["bookmarks"] = False
    return render(request, 'bookmarks.html', context)

def add_msg_bookmark(request, id):
    try:
        msg = Message.objects.get(id=id)
        if msg.thread.node.type_private and (request.user != msg.thread.user or not request.user.has_perm('forum.view_thread')):
            return redirect('section', msg.thread.node.slug)
    except:
        return render(request, 'error.html')
    try:
        exists = Bookmark.objects.get(user=request.user, forum_msg=msg)
    except:
        bookmark = Bookmark.objects.create(user=request.user, forum_msg=msg)
        bookmark.save()
    # url = reverse('msg_redirect', args=(msg.thread.node.slug, msg.thread.slug, msg.thread.id, msg.id))
    # print(url)
    return redirect('msg_redirect', msg.thread.node.slug, msg.thread.slug, msg.thread.id, msg.id)


def del_bookmark(request, id):
    try:
        bookmark = Bookmark.objects.get(user=request.user, id=id).delete()
    except:
        pass
    return redirect('bookmarks_main')
    