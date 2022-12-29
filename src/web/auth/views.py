from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login, logout, authenticate
# Create your views here.


def index(request):
    return render(request, 'auth/index.html')


def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()

    return render(request, 'registration/signup.html', {"form": form})
