from django.shortcuts import render,redirect
from . import form
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
# def add_author(request):
#     if request.method=='POST':
#         author_form = form.AuthorForm(request.POST)
#         if author_form.is_valid():
#             author_form.save()
#             return redirect('add_author')
#     else:
#         author_form = form.AuthorForm(request.POST)
#     return render(request,'add_author.html',{'form': author_form })
def register(request):
    if request.method=='POST':
        register_form = form.RegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request,'Account Created SUCCESSFUL')
            return redirect('register')
    else:
        register_form = form.RegisterForm()
    return render(request,'register.html',{'form': register_form,'type':'Register' })

def user_login(request):

    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            userpass = form.cleaned_data['password']

            user = authenticate(username=name, password=userpass)

            if user is not None:
                messages.success(request,'Log in SUCCESSFUL')

                login(request, user)
                return redirect('profile')
            else:
                messages.warning(request,'Login information SUCCESSFUL')
                return redirect('register')

    else:
        form = AuthenticationForm()

    return render(request, 'register.html', {'form': form, 'type':'Login'})
@login_required
def profile(request):
    if request.method == 'POST':
        profile_form = form.ChangeUserForm(request.POST, instance = request.user)
        if profile_form.is_valid():
            use = profile_form.save()
            messages.success(request, "accound change successfully")
                # messages.warning(request, "worning")
                # messages.info(request, "infor")
            
            return redirect('profile')
                # print("Saved Successfully")
                # print(use)
    else:
        profile_form = form.ChangeUserForm(request.user)
    return render(request,'profile.html',{'form':profile_form})

    



# def userlogout(request):
#     logout(request)
#     return redirect('login')
# def pass_change(request):
#     if request.user.is_authenticated:
#         if request.method == 'POST':
#             form = PasswordChangeForm(user=request.user,data= request.POST)
#             if form.is_valid():
#                 form.save()
#                 update_session_auth_hash(request,form.user) #password update korbe
#                 return redirect('profile')
#         else:
#             form = PasswordChangeForm(user=request.user)
#         return render(request,'passchage.html',{'form':form})
#     else:
#         return redirect('login')
# def pass_change2(request):
#     if request.user.is_authenticated:
#         if request.method == 'POST':
#             form = SetPasswordForm(user=request.user,data= request.POST)
#             if form.is_valid():
#                 form.save()
#                 update_session_auth_hash(request,form.user) #password update korbe
#                 return redirect('profile')
#         else:
#             form = SetPasswordForm(user=request.user)
#         return render(request,'passchage.html',{'form':form})
#     else:
#         return redirect('login')
# def change_user_data(request):
#     if request.user.is_authenticated:
#         if request.method == 'POST':
#             form = ChangeUser(request.POST, instance = request.user)
#             if form.is_valid():
#                 messages.success(request, "accound change successfully")
#                 # messages.warning(request, "worning")
#                 # messages.info(request, "infor")
#                 use = form.save()
#                 # print("Saved Successfully")
#                 # print(use)
#         else:
#             form = ChangeUser()
#         return render(request,'profile.html',{'form':form})
#     else:
#         return redirect('signup')



        



