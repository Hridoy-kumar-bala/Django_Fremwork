from django.shortcuts import render,redirect
from .forms import RegisterUserForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, SetPasswordForm, PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Account created successfully")
            return redirect('login') 
    else:
        form = RegisterUserForm()

    return render(request, 'signup.html', {'form': form})
def user_login(request):
    if request.method =='POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user =form.get_user()
            login(request,user)
            messages.success(request,"Logged In successfully")
            return redirect('profile')
    else:
        form =AuthenticationForm()
    return render(request, 'login.html',{'form':form})
@login_required
def profile(request):
    return render(request, 'profile.html')
@login_required
def user_logout(request):
    logout(request)
    messages.success(request,"Loguot successfully ")
    return redirect('homepage')
@login_required
def change_password(request):
    if request.method=='POST':
        form = PasswordChangeForm(user=request.user,data=request.POST)
        if form.is_valid():
            user =form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "password changed successfully")
            return redirect('profile')
    else:
        form = PasswordChangeForm(user= request.user)

    return render(request,'change_password.html',{'form':form})
@login_required
def change_password_without_old(request):
    if request.method == "POST":
        form = SetPasswordForm(request.user, request.POST)

        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Password changed successfully")
            return redirect("profile")

    else:
        form = SetPasswordForm(request.user)

    return render(request, "change_password2.html", {"form": form})




