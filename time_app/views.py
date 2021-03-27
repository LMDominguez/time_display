from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

def index(request):
    return render(request, "index.html")

def time(request):
    context = {
        "time": strftime("%Y-%m-%d %I:%M %p", gmtime()),
    }
    return render(request, "time_display.html", context)
