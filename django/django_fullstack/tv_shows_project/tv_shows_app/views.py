from django.shortcuts import redirect, render
from . import models
from django.contrib import messages

# Create your views here.
def all_shows(request):
    context = {
        'shows': models.all_shows()
    }

    return render(request, 'all_shows.html', context)

def create_show(request):
    if request.method == "POST":
        errors = models.Show.objects.validator(request.POST)

        if len(errors) > 0:
            
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f'/shows/new')

        else:
            messages.success(request, "Show successfully created")
            id = models.create(request.POST)
            return redirect(f'/shows/{id}')

        

    return redirect('/shows')

def add(request):
    return render(request, 'new_show_form.html')

def single_show(request, id):
    context = models.single_show(id)

    return render(request, 'show_details.html', context)

def edit(request, id):
    context = {
        'id': id
    }
    return render(request, 'edit_show.html', context)

def update(request, id):
    errors = models.Show.objects.validator(request.POST)

    if len(errors) > 0:
        
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/shows/{id}/edit')

    else:
        models.update(id, request.POST)
        messages.success(request, "Show successfully updated")
        return redirect(f'/shows/{id}')

def delete(request, id):
    models.delete(id)
    return redirect('/shows')

