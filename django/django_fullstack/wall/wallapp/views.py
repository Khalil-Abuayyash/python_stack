from django.shortcuts import render, redirect
from . import models
# Create your views here.

def wall(request):
    context = {
        'user': models.User.objects.get(id=request.session['id']),
        'posts': models.Message.objects.all()
    }
    return render(request, "wall.html", context)

def create_message(request):
    if request.method == "POST":
        models.create_message(request.POST, request.session['id'])
    return redirect('/wall')

def create_comment(request):
    if request.method == "POST":
        models.create_comment(request.POST, request.session['id'])
    return redirect('/wall')