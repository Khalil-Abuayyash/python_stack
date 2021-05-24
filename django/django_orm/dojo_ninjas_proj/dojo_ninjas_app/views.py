from django.shortcuts import redirect, render, HttpResponse
from .models import Dojo, Ninja

# Create your views here.

def index(request):
    
    context = {
        'dojos': Dojo.objects.all()
    }

    return render(request, 'index.html', context)

def create(request):
    if request.method == "POST":
        if request.POST['model'] == "dojo":
            Dojo.objects.create(name=request.POST['name'], city=request.POST['city'], state=request.POST['state'])
        
        if request.POST['model'] == "ninja":
            Ninja.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], dojo= Dojo.objects.get(id=request.POST['dojo_id']))
    
    return redirect('/')