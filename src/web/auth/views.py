from django.shortcuts import render
from .forms import RegisterForm
# Create your views here.


def index(request):
    return render(request, 'auth/index.html')


def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
    else:
        form = RegisterForm()

    return render(request, 'registration/signup.html', {"form": form})
