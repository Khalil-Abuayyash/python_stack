from django.shortcuts import redirect, render
import random
from time import gmtime, strftime

# Create your views here.

def index(request):
    if 'golds' not in request.session:
        request.session['golds'] = 0
    
    if 'activities' not in request.session:
        request.session['activities'] = []


    context = {
        'golds' : request.session['golds'],
        'activities': request.session['activities']
    }

    return render(request, 'index.html', context)

def process(request):
    
    if request.method == "POST":
        earned_time = strftime("%Y-%m-%d %H:%M %p")

        if request.POST['place'] == 'farm':
            num = random.randint(10,20)
            request.session['golds'] += num
            request.session['activities'].append(f'Earned {num} golds from the farm! ({earned_time})')
            return redirect('/')
            

        if request.POST['place'] == 'cave':
            num = random.randint(5,10)
            request.session['golds'] += num
            request.session['activities'].append(f'Earned {num} golds from the cave! ({earned_time})')
            return redirect('/')

        if request.POST['place'] == 'house':
            num = random.randint(2,5)
            request.session['golds'] += num 
            request.session['activities'].append(f'Earned {num} golds from the house! ({earned_time})')
            return redirect('/')

        if request.POST['place'] == 'casino':
            num = random.randint(-50,50)
            request.session['golds'] += num

            if num > 0:
                request.session['activities'].append(f'Earned {num} golds from the casion! ({earned_time})')
            elif num < 0:
                request.session['activities'].append(f'Eentered the casino and lost {num} golds... Ouch.. ({earned_time})')
            else:
                request.session['activities'].append(f'Eentered the casino and left with golds unchanged  ({earned_time})')

            return redirect('/')