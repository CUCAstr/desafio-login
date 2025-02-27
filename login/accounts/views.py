from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
import re
from .forms import CustomUserCreationForm

# Create your views here.
def indexView(request):
    return render(request, 'index.html')

@login_required
def dashboardView(request):
    return render(request, 'dashboard.html')

def registerView(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.email  # Set username as email
            user.save()
            messages.success(request, "Registration successful. Please log in.")
            return redirect('login_url')
        else:
            messages.error(request, "Registration failed. Please correct the errors above.")
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def loginView(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.get(email=email)
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Login successful.")
                return redirect('menu')
            else:
                messages.error(request, "Incorrect password.")
        except User.DoesNotExist:
            messages.error(request, "Email does not exist.")
    return render(request, 'registration/login.html')

def menuView(request):
    return render(request, 'menu.html')

def logoutView(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login_url')