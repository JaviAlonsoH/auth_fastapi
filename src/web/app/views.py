import os
import requests

from .forms import RegisterForm, PostForm
from .models.property_models import Post

from pathlib import Path
from web import settings

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User, Group
from django.contrib.auth import login, logout, authenticate

from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes

from fastapi.templating import Jinja2Templates
# Create your views here.

templates = Jinja2Templates(
    directory="C:/Users/Usuario/Documents/Git Repositories/auth_fastapi/src/web/app/templates")


@login_required(login_url="/app/login")
def home(request):
    posts = Post.objects.all()

    if request.user.is_authenticated:
        return render(request, 'app/home.html', {"posts": posts})


@login_required(login_url="/app/login")
# @permission_required("app.add_property", login_url="/login", raise_exception=True)
def create_property(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save
            post.author = request.user
            return redirect('app/home')
    else:
        form = PostForm()

    return render(request, 'app/create_post.html', {"form": form})


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
