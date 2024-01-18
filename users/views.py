from django.shortcuts import render, redirect

from users.forms import SignupForm, LoginForm


def profile(request):
    context = {'title': 'Home - Профиль'}
    return render(request, 'users/profile.html', context)


def logout(request):
    context = {'title': 'Home - Выход'}
    return render(request, '', context)


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
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/')
    else:
        form = LoginForm()

    return render(request, 'users/login.html', {
        'form': form
    })
