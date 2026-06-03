from django.shortcuts import render

def home(request):
    return render(request,'base.html')
def about(request):
    return render(request, 'first_app/about.html')

# views.py