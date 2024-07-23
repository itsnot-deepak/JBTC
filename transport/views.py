from django.shortcuts import render
from .models import LoadInfo
from .forms import LoadInfoForm

def home(request):
    return render(request, 'transport/home.html')

def about(request):
    return render(request, 'transport/about.html')

def contact(request):
    return render(request, 'transport/contact.html')

def load_form(request):
    if request.method == "POST":
        form = LoadInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'transport/thank_you.html')
    else:
        form = LoadInfoForm()
    return render(request, 'transport/load_form.html', {'form': form})
