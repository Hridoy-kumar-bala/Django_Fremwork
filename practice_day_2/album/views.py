from django.shortcuts import render, redirect
from album.models import Album
from . import form

# ADD ALBUM
def add_album(request):
    if request.method == "POST":
        album_form = form.AlbumForm(request.POST)

        if album_form.is_valid():
            album_form.save()
            print("SAVED SUCCESSFULLY")
            return redirect('homepage')
        else:
            print("ERROR:", album_form.errors)

    else:
        album_form = form.AlbumForm()

    return render(request, 'add_album.html', {'form': album_form})
# EDIT
def edit(request, id):
    album = Album.objects.get(pk=id)

    if request.method == "POST":
        album_form = form.AlbumForm(request.POST, instance=album)
        if album_form.is_valid():
            album_form.save()
            return redirect('homepage')
    else:
        album_form = form.AlbumForm(instance=album)

    return render(request, 'add_album.html', {'form': album_form})


# DELETE
def delete(request, id):
    album = Album.objects.get(pk=id)
    album.delete()
    return redirect('homepage')