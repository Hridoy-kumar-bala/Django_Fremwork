from django.shortcuts import render,redirect
from . import form
from . import models
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def add_posts(request):
    if request.method=='POST': #user post request korche
        post_form = form.PostForm(request.POST) #user er post request data ekhane capture korlam
        if post_form.is_valid():#post kora data gulo amra valid kina check kortechi
            # post_form.changed_data['author'] = request.user
            post_form.instance.author =request.user
            post_form.save() #jodi data gulo valid hoy taile database e save korbo
            return redirect('add_posts') # sob thik thakle take add author er url e pathiye dibo
    else: #user normally website e gele blank form pabe
        post_form = form.PostForm(request.POST)
    return render(request,'add_category.html',{'form': post_form })
@login_required
def edit_posts(request,id):
    post = models.Post.objects.get(pk=id)
    post_form = form.PostForm(instance=post)
    if request.method=='POST':
        post_form = form.PostForm(request.POST,instance=post)
        if post_form.is_valid():
            post_form.instance.author =request.user
            post_form.save()
            return redirect('homepage')
    return render(request,'add_category.html',{'form': post_form })
@login_required
def delete_post(request,id):
    post = models.Post.objects.get(pk=id)
    post.delete()
    return redirect('homepage')