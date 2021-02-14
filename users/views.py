from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth.forms import AuthenticationForm


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Successfully created account for {username}')
            return redirect('/')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})


def c_login(request):
    if request.GET:
        user = authenticate(request, username=request.GET['username'], password=request.GET['password'])
        if user:
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()
        return render(request, 'users/login.html', {'form': form})


def c_logout(request):
    logout(request)
    messages.success(request, 'Successfully logged out')
    return redirect('/')
