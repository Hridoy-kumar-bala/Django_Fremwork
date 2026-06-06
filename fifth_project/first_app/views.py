from django.shortcuts import render
from . forms import contactForm, studentData, PasswordValidationProject
def index(request):
    return render(request, 'first_app/index.html')
def submit_form(request):
    return render(request, 'first_app/from.html')
def about(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        rank = request.POST.get('rank')
        return render(request, 'first_app/about.html', {'name': name, 'email': email, 'rank': rank})
    else:
        return render(request, 'first_app/about.html')
# def submit_form1(request):
#     return render(request, 'first_app/from1.html')
# def about1(request):
#     if request.method == 'POST':
#         print(request.POST)
#         name = request.POST.get('get_username')
#         email = request.POST.get('get_email')
#         select = request.POST.get('select')
#         return render(request, 'first_app/get_about.html', {'name': name, 'email': email , 'select': select})
#     else:
#         return render(request, 'first_app/get_about.html')

def DjangoForm(request):
    # form=contactForm()
    if request.method =='POST': #data is store
        form=contactForm(request.POST, request.FILES) 
        if form.is_valid():
            # file = form.cleaned_data['files']
            # with open('first_app/upload/' + file.name, 'wb+') as destination:
            #     for chunk in file.chunks():
            #         destination.write(chunk)

            print(form.cleaned_data)
            # return render(request,'first_app/django_from.html',{'form':form})
    else:
        form =contactForm()
    return render(request,'first_app/django_from.html',{'form':form})

def StudentFrom(request):
    if request.method == 'POST':
        form = studentData(request.POST,request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = studentData()

    return render(request, 'first_app/django_home.html', {'form': form})

# def StudentFrom(request):
#     form = studentData()
#     return render(request, 'first_app/django_from.html', {'form': form})

def PasswordValidation(request):
    if request.method == 'POST':
        form = PasswordValidationProject(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = PasswordValidationProject()

    return render(request, 'first_app/django_home.html', {'form': form})
