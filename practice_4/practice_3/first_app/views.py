from django.shortcuts import render
from .forms import FromPage

def home(request):
    if request.method == 'POST':
        form = FromPage(request.POST)

        if form.is_valid():
            print(form.cleaned_data)

    else:
        form = FromPage()

    return render(request, 'form.html', {'form': form})