from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def courses(request):
    return HttpResponse('this is courses page. ')
def about(request):
    return HttpResponse('this is about page. ')
def firstapp(request):
    return HttpResponse('this is FIRST APP page. ')