from django.shortcuts import render,redirect
from . import form
# Create your views here.
def add_posts(request):
    if request.method=='POST':
        post_form = form.PostForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect('add_posts')
    else:
        post_form = form.PostForm(request.POST)
    return render(request,'add_category.html',{'form': post_form })