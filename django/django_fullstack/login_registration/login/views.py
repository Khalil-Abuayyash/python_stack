from django.contrib.messages.api import error
from django.db import models
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == "POST":

        if request.POST['operation'] == "login":
            errors = User.objects.validator_login(request.POST)

            if len(errors) > 0:
                for key, value in errors.items():
                    messages.error(request, value)
                return redirect('/')
            else:
                user_details = get_user_details(request.POST['email'])
                for key, value in user_details.items():
                    request.session[key] = value

                messages.success(request, "Logged in successfully")
                return redirect(f"/success")

        if request.POST['operation'] == "register":
            request.session.clear()
            errors = User.objects.validator_registeration(request.POST)
            if len(errors) > 0 :
                for key, value in errors.items():
                    messages.error(request, value)
                return redirect('/')
            else:
                create_user(request.POST)
                messages.success(request, "user successfully created")
                request.session['first_name'] = request.POST['first_name']
                return redirect('/success')
    return redirect('/')
            

def show_user_page(request):
    if 'email' in request.session:
        return render(request, 'success.html')

    if 'first_name' in request.session:
        return render(request, 'success.html')
        
    else:
        return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')