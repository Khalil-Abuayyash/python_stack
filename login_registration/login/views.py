from django.shortcuts import render, redirect
from .models import User

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == "POST":

        if request.POST['operation'] == "login":
            user = User.objects.get(name=request.POST['name'])

            if user.password == request.POST['password']:
                return redirect(f"/{user.name}")

        if request.POST['operation'] == "register":
            User.objects.create(name=request.POST['name'], password=request.POST['password'])
            return redirect('/')

def show_user_page(request, name):
    user = User.objects.get(name = name)
    context = {
        'name': user.name,
        'password': user.password
    }

    return render(request, 'user.html', context)




    return redirect('/')