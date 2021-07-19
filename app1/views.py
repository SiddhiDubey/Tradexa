from django.contrib.auth import models
from app1.forms import RegisterForm
from django import forms
from django.contrib.auth.backends import UserModel
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CreatePost, RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.views.generic import FormView


from .forms import *
from .models import *


# Create your views here.

def app1(request):

	context = {}
	return render(request, 'main.html', context)



def registerPage(request):
    if(request.method == 'POST'):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, f'Account was created for ' + user)
            return redirect ('postPage')
    else:
         form = RegisterForm()
    return render (request, 'register.html',{'form': form})

def loginPage(request):


    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, username)
            return redirect('postPage')
        else:
            messages.info(request, 'Username or Password is Incorrect')

    context = {}
    return render(request, 'login.html', context)



def postPage(request):
    if(request.method == 'POST'):
        form = CreatePost(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            return redirect ('app1')
    else:
         form = CreatePost()
    return render (request, 'create_post.html',{'form': form})


