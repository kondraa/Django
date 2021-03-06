from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import  reverse

# Create your views here.
from .forms import UserLoginForm, UserRegisterForm


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user.is_active:
                print('is_active')
                auth.login(request, user)
                return HttpResponseRedirect(reverse('mainapp:index'))
            else:
                print('is_not_active')
        else:
            print(form.errors)
    else:
        form = UserLoginForm()
    context = {
        'title': 'Geekshop Authorization',
        'form': form,
    }
    return render(request, 'users/login.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:login'))
        else:
            print(form.errors)
    else:
       form = UserRegisterForm()
    context = {
        'title': 'Geekshop Registration',
        'form': form,
    }
    return render(request, 'users/register.html', context)