from django.shortcuts import render, redirect
from .models import User
from .forms import SignupForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth

# Create your views here.
def signup(request):
   if request.method == 'GET':
      form = SignupForm()
      context = {'form': form}
      return render(request, 'users/signup.html', context)
   else:
      form = SignupForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect('post:main')
      else:
         context = {'form': form}
         return render(request, 'users/signup.html', context)

def login(request):
   if request.method == 'GET':
      form = AuthenticationForm()
      context = {'form': form}
      return render(request, 'users/login.html', context)
   else:
      form = AuthenticationForm(request, request.POST)
      if form.is_valid():
         auth.login(request, form.get_user())
         return redirect('post:main')
      else:
         context = {'form': form}
         return render(request, 'users/login.html', context)

def logout(request):
   auth.logout(request)
   return redirect('post:main')
