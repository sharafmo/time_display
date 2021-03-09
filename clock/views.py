from django.shortcuts import render, HttpResponse
from time import gmtime, strftime

def home(request):
    context = {
        "date": strftime("%Y-%m-%d", gmtime()),
        "time": strftime("%H:%M %p", gmtime())
    }
    return render(request, "index.html", context)


