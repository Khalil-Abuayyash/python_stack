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
                return redirect(f"/books")

        if request.POST['operation'] == "register":
            if 'first_name' or 'email' in request.session:
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
                return redirect('/books')
    return redirect('/')
            

def welcome(request):
    if 'email' in request.session:
        context = {
            'books': get_all_books(),
            'fav_books': get_fav_books(request.session['email'])
        }
        return render(request, 'welcome.html', context)

    if 'first_name' in request.session:
        return render(request, 'welcome.html', context)
        
    else:
        return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')

def add_book(request):
    if request.method == 'POST':
        errors = Book.objects.validator(request.POST)
        if len(errors) > 0 :
            for key, value in errors.items():
                messages.error(request, value)
            
        else :
            messages.success(request, 'The book has been added correctly')
            create_book(request.POST, request.session['email'])
    
    return redirect('/books')

def show_book_details(request, book_id):
    context = {
        'book' : get_book_details(book_id),
        'fav_books': get_fav_books(request.session['email']),

    }
    return render(request, 'book_details.html', context)

def add_to_fav(request, book_id):
    favorite_book(request.session['id'], book_id)
    return redirect('/books')

def edit(request, book_id):
    if request.method == 'POST':
        edit_book(book_id, request.POST)
        return redirect(f'/books/{book_id}')

def delete(request, book_id):
    delete_book(book_id)
    return redirect('/books')