from django.shortcuts import render,redirect
from .import form
from . import models
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
def edit(request,id):
    post = models.Musician.objects.get(pk=id)
    musician_form = form.MusicianForm(instance=post)
    if request.method=='POST':
        musician_form = form.MusicianForm(request.POST,instance=post)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('homepage')
    return render(request,'add_musician.html',{'form': musician_form })
def delete(request,id):
    post = models.Musician.objects.get(pk=id)
    post.delete()
    return redirect('homepage')

