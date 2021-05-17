from django.shortcuts import render
from time import gmtime, strftime

# Create your views here.
def showTD(request):
    context = {
        "time": strftime("%Y-%m-%d"),
        "date": strftime("%H:%M %p")
    }
    return render(request, 'index.html', context)