from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import auth, messages
import shiny.views

from users.forms import SignupForm, LoginForm


def profile(request):
    context = {'title': 'Home - Профиль'}
    return render(request, 'users/profile.html', context)


def registration(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'users/registration.html', {
        'form': form
    })


def login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)

        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('shiny:index'))

    else:
        form = LoginForm()

    context = {
        'title': 'Home - Авторизация',
        'form': form
    }

    return render(request, 'users/login.html', context)


@login_required
def logout(request):
    auth.logout(request)
    return redirect(reverse('users:login'))