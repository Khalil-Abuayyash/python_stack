from django.shortcuts import redirect, render
from . import models

# Create your views here.
def all_shows(request):
    context = {
        'shows': models.all_shows()
    }

    return render(request, 'all_shows.html', context)

def create_show(request):
    if request.method == "POST":
        id = models.create(request.POST)
        return redirect(f'/shows/{id}')

    return redirect('/shows')

def add(request):
    return render(request, 'new_book_form.html')

def single_show(request, id):
    context = models.single_show(id)

    return render(request, 'show_details.html', context)

def edit(request, id):
    context = {
        'id': id
    }
    return render(request, 'edit_show.html', context)

def update(request, id):
    context = models.update(id, request.POST)
    return redirect(f'/shows/{id}')

def delete(request, id):
    models.delete(id)
    return redirect('/shows')