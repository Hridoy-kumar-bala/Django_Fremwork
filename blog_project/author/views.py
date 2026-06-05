from django.shortcuts import render,redirect
from . import form
# Create your views here.
def add_author(request):
    if request.method=='POST':
        author_form = form.AuthorForm(request.POST)
        if author_form.is_valid():
            author_form.save()
            return redirect('add_author')
    else:
        author_form = form.AuthorForm(request.POST)
    return render(request,'add_author.html',{'form': author_form })