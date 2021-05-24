from django.shortcuts import redirect, render

# Create your views here.
def index(request):
    if 'is_log' in request.session:
        return render(request, 'welcome.html')
    return render(request, 'index.html')

def login(request):
    
    if request.method == "POST" and request.POST['form_type'] == 'login' :
        print('login')
        is_checked = check_credentials(request.POST['username'], request.POST['pass'])
        if is_checked:
            print('checked')
            request.session['username'] = request.POST['username'] 
            request.session['is_log'] = True
            return redirect('/welcome')
            

    if request.method == "POST" and request.POST['form_type'] == 'register':
        pass

    return redirect('/')

def welcome(request):
    if 'username' in request.session:
        return render(request, 'welcome.html')
    return redirect('/')

def check_credentials(username, password):
    if username == "root" and password == "root":
        return True
    return False

def register(username, password):
    return username

def logout(request):
    request.session.clear()