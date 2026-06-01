import datetime

from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # return HttpResponse("Home Page Working")
    d={'author':'Hridoy','age': 22, 'lst': ['python','is','best'],'birthday': datetime.datetime.now(), 'publication':'', 'course': [
        {'id': 1, 'name': 'Python', 'price': 1000},
        {'id': 2, 'name': 'Django', 'price': 2000},
        {'id': 3, 'name': 'React', 'price': 3000},
    ], 'TEXT':'THIS IS HRIDOY KUMAR BALA'}

    return render(request,'home.html',d)
