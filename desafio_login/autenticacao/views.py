from django.shortcuts import render

# Create your views here.
def login_view(request):
    return render(request, 'autenticacao/login.html')

def registrar_view(request):
    return render(request, 'autenticacao/registrar.html')

def menu_view(request):
    return render(request, 'autenticacao/menu.html')
