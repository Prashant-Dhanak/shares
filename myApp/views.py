from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def index(request):
    return render(request, "myApp/index.html")

def greet(request, name):
    return render(request, "myApp/greet.html", {
        "name": name.capitalize()
    })
