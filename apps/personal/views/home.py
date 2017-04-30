from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def home(request):

    context = {
        'characters': 'characters',
    }

    return render(request, 'sitehome.html', context)