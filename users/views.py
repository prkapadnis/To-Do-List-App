from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import UserRegistration


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/Note/home')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data.get(
                'username'), password=form.cleaned_data.get('password'))
            if user is not None:
                login(request, user)
                return redirect('/Note/home')
            else:
                messages.error(request, f"Invalid Username or Password!")
        else:
            messages.error(request, f"Invalid Username or Password!")
    else:
        form = AuthenticationForm()
    context = {'form': form}
    return render(request, "user/login_view.html", context)


def register_view(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'Successfully registered with the {form.instance.username} username')
            return redirect('/')
    else:
        form = UserRegistration()
    context = {'form': form}
    return render(request, 'user/register_view.html', context)


def logout_view(request):
    logout(request)
    return redirect('/')
