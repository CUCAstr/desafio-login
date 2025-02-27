from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import re

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, error_messages={'required': 'Este campo é obrigatório.', 'invalid': 'Digite um endereço de email válido.'})
    name = forms.CharField(max_length=30, required=True, error_messages={'required': 'Este campo é obrigatório.'})
    password1 = forms.CharField(
        label="Senha",
        strip=False,
        widget=forms.PasswordInput,
        help_text="A senha deve ter pelo menos 8 caracteres, conter um número, uma letra maiúscula e um caractere especial.",
        error_messages={
            'required': 'Este campo é obrigatório.',
            'min_length': 'A senha é muito curta. Deve conter pelo menos 8 caracteres.',
        },
    )
    password2 = forms.CharField(
        label="Confirmar Senha",
        strip=False,
        widget=forms.PasswordInput,
        help_text="Digite a mesma senha que antes, para verificação.",
        error_messages={
            'required': 'Este campo é obrigatório.',
        },
    )

    class Meta:
        model = User
        fields = ("name", "email", "password1", "password2")

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not re.match("^[A-Za-z]*$", name):
            raise forms.ValidationError("O nome deve conter apenas letras.")
        return name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise forms.ValidationError("Digite um endereço de email válido.")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("O email já existe.")
        return email

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        errors = []
        if len(password1) < 8:
            errors.append("A senha deve ter pelo menos 8 caracteres.")
        if not re.search(r'\d', password1):
            errors.append("A senha deve conter pelo menos 1 número.")
        if not re.search(r'[A-Z]', password1):
            errors.append("A senha deve conter pelo menos 1 letra maiúscula.")
        if not re.search(r'\W', password1):
            errors.append("A senha deve conter pelo menos 1 caractere especial.")
        if errors:
            raise forms.ValidationError(errors)
        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("As senhas não coincidem.")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['email']  # Set username as email
        if commit:
            user.save()
        return user
