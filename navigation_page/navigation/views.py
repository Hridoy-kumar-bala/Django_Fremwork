from django.shortcuts import render

from django.shortcuts import render

def index(request):
    return render(request, 'navigation/index.html')

def about(request):
    return render(request, 'navigation/about.html')

def contact(request):
    return render(request, 'navigation/contact.html')