from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
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
            messages.success(request, "Registro bem-sucedido. Por favor, faça login.")
            return redirect('login_url')
        else:
            messages.error(request, "Falha no registro. Por favor, corrija os erros acima.")
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
                messages.success(request, "Login bem-sucedido.")
                return redirect('menu')
            else:
                messages.error(request, "Senha inválida.")
        except User.DoesNotExist:
            messages.error(request, "E-mail inexistente.")
    return render(request, 'registration/login.html')

def menuView(request):
    return render(request, 'menu.html')

def logoutView(request):
    logout(request)
    messages.success(request, "Você saiu do sistema.")
    return redirect('login_url')