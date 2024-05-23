from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# from users.models import Warnings_history

# different forums sections (t.ex: main or question)
class Node(models.Model):
    name = models.CharField(max_length=225)
    slug = models.SlugField(max_length=225, blank=True, null=True)
    description = models.TextField(blank=True, default=None, null=True)
    type_question = models.BooleanField(default=False)
    type_private = models.BooleanField(default=False)
    user_only = models.BooleanField(default=False)
    staff_only = models.BooleanField(default=True)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class Thread(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=225)
    slug = models.SlugField(max_length=225, blank=True, null=True)
    node = models.ForeignKey(Node, on_delete=models.CASCADE)
    is_closed = models.BooleanField(default=False)
    is_visible = models.BooleanField(default=True)
    is_pinned = models.BooleanField(default=False)
    msg_amount = models.IntegerField(blank=True, null=True, default=1)
    invis_reason = models.TextField(blank=True, null=True)
    deleted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="thread_deleted_by")
    time_created = models.DateTimeField(default=datetime.now())
    time_changed = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
class Message(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    is_start = models.BooleanField(default=False)
    upvotes = models.PositiveIntegerField(null=True, blank=True, default=0)
    downvotes = models.PositiveIntegerField(null=True, blank=True, default=0)
    is_solution = models.BooleanField(default=False)
    is_visible = models.BooleanField(default=True)
    deleted_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name="deleted_by")
    invis_reason = models.TextField(blank=True, null=True)
    # warning = models.OneToOneField(Warnings_history, on_delete=models.SET_NULL, null=True, blank=True)
    time_created = models.DateTimeField(default=datetime.now())
    time_changed = models.DateTimeField(null=True, blank=True)
    changer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="changer")

    def __str__(self):
        return f'{self.user} - {self.thread}'
    
class Attachment(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    filename = models.CharField(max_length=225)

    def __str__(self):
        return f'attachment {self.id}'