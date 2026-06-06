from django.shortcuts import render,redirect
from . import models
from first_app.forms import StudentForm
# Create your views here.
def home(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        # if form.is_valid():
        #     form.save(commit=False)
        #     print(form.cleaned_data)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)

    return render(request,"home.html", {'form': form})
