from django.shortcuts import render
import random

num = random.randint(1, 100)

def root(request):
    context = {
        'text': '',
        'color': 'white'
    }
    return render(request, 'index.html',context)

def compare(request):
    context = {
        'text': '',
        'color': 'white'
    }
    if request.method == 'POST':
        number = int(request.POST['number'])
        if number >= 0 and number <= 100:

            if number == num:
                s = num, " was the number!"
                context = {
                    'text': s,
                    'color': 'green'
                }
                return render(request, 'index.html',context)
            elif number > num :
                context = {
                    'text': "Too High!",
                    'color': 'red'
                }
                return render(request, 'index.html',context)
            else:
                context = {
                    'text': "Too Low!",
                    'color': 'red'
                }
                return render(request, 'index.html',context)
        return render(request, 'index.html',context)
    return render(request, 'index.html',context)
