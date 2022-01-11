from django.shortcuts import render

# Create your views here.
from .forms import UserLoginForm


def login(request):
    form = UserLoginForm()
    context = {
        'title': 'Geekshop Authorization',
        'form': form,

    }
    return render(request, 'users/login.html', context)


def register(request):
    context = {
        'title': 'Geekshop Registration'
    }
    return render(request, 'users/register.html', context)