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
    except:
        return render(request, 'error.html')
    try:
        exists = Bookmark.objects.get(user=request.user, forum_msg=msg)
    except:
        bookmark = Bookmark.objects.create(user=request.user, forum_msg=msg)
        bookmark.save()
    url = reverse('msg_redirect', args=(slugify(msg.thread.node.name), slugify(msg.thread.title), msg.thread.id, msg.id)).replace('%23', '#')
    return redirect(url)


def del_bookmark(request, id):
    try:
        bookmark = Bookmark.objects.get(user=request.user, id=id).delete()
    except:
        pass
    return redirect('bookmarks_main')
    