from django.shortcuts import render,redirect
from . import form
from . import models
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
def edit_posts(request,id):
    post = models.Post.objects.get(pk=id)
    post_form = form.PostForm(instance=post)
    if request.method=='POST':
        post_form = form.PostForm(request.POST,instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('homepage')
    return render(request,'add_category.html',{'form': post_form })
def delete_post(request,id):
    post = models.Post.objects.get(pk=id)
    post.delete()
    return redirect('homepage')