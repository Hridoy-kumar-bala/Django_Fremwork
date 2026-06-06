from django.http import HttpResponse

def home(resquest):
    return HttpResponse("this is home page")

def contact(request):
    return HttpResponse("this is contact page")

 