from django.shortcuts import redirect, render

# Create your views here.

def root(request):
    if 'visits' in request.session:
        request.session['visits'] += 1
    else:
        request.session['visits'] = 1
    context = {
        'visits' : request.session['visits']
    }
    return render(request, 'index.html', context)

def clear(request):
    request.session.clear()
    return redirect('/')
