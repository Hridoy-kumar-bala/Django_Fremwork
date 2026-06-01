from django.shortcuts import render

def homepage(request):
    return render(request,'navigation/home.html')
def about(request):
    return render(request,'navigation/about.html')

def contact(request):
    return render(request,'navigation/contact.html')
