from django.shortcuts import render,redirect
from .import form
# Create your views here.
# ADD MUSICIAN
def musician(request):
    if request.method == "POST":
        musician_form = form.MusicianForm(request.POST)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('homepage')
    else:
        musician_form = form.MusicianForm()

    return render(request, 'add_musician.html', {'form': musician_form})

