from django.core.checks import messages
from django.db import models
from django.db.models.deletion import CASCADE
from login_registeration.models import *

# Create your models here.

class Message(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, related_name="messages", on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    text = models.TextField()
    message = models.ForeignKey(Message, related_name="comments", on_delete=CASCADE)
    user = models.ForeignKey(User, related_name="comments", on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def create_message(data, id):
    text = data['text']
    user = User.objects.get(id=id)
    Message.objects.create(text=text, user=user)

def create_comment(data, id):
    text = data['text']
    user = User.objects.get(id=id)
    Comment.objects.create(text=text, user=user)