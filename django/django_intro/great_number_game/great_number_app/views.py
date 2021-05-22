from django.shortcuts import redirect, render
import random

num = random.randint(1, 100)

def root(request):
    if 'text' in request.session and 'color' in request.session:

        context = {
            'text': request.session['text'],
            'color': request.session['color']
        }
    else:
        context = {
            'text': '',
            'color': 'white'
        }

    return render(request, 'index.html',context)

def compare(request):

    if request.method == 'POST':
        number = int(request.POST['number'])
        if number >= 0 and number <= 100:

            if number == num:
                s = num, " was the number!"
                request.session['color'] = 'green'
                request.session['text'] = s

                return redirect('/')

            elif number > num :
                
                request.session['color'] = 'red'
                request.session['text'] = "Too High!"

                return redirect('/')

            else:
                
                request.session['color'] = 'red'
                request.session['text'] = "Too Low!"
                
                return redirect('/')

        return redirect('/')
    return redirect('/')
