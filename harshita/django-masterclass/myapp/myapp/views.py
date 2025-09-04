from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("<h1>Welcome to our home page</h1>")
    return render(request, "website/index.html")

def about(request):
    # return HttpResponse("<h1>Welcome to our about page</h1>")
    return render(request, "website/about.html")

def contact(request):
    # return HttpResponse("<h1>Welcome to our contact page</h1>")
    return render(request, "website/contact.html")
