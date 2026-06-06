from django.shortcuts import render, redirect
from .forms import FormPage
from .models import MyModel

def home(request):

    if request.method == 'POST':
        form = FormPage(request.POST)

        if form.is_valid():
            obj= MyModel.objects.create(
                name=form.cleaned_data['name'],
                comment=form.cleaned_data['comment'],
                comments=form.cleaned_data['comments'],
                email=form.cleaned_data['email'],
                agree=form.cleaned_data['agree'],
                date=form.cleaned_data['date'],
                birth_date=form.cleaned_data['birth_date'],
                value=form.cleaned_data['value'],
                email_address=form.cleaned_data['email_address'],
                message=form.cleaned_data['message'],
                email_address2=form.cleaned_data['email_address2'],
                first_name=form.cleaned_data['first_name'],
                day=form.cleaned_data['day'],
                favorite_color=form.cleaned_data['favorite_color'],
                favorite_colour=form.cleaned_data['favorite_colour'],
                favorite_colors=",".join(form.cleaned_data['favorite_colors']),
            )

            return redirect('show', pk=obj.id)

    else:
        form = FormPage()

    return render(request, 'from.html', {'form': form})
def show(request, pk):
    data = MyModel.objects.get(id=pk)
    return render(request, 'show.html', {'data': data})
def all_data(request):
    data = MyModel.objects.all()
    return render(request, 'all.html', {'data': data})