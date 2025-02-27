from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import re

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ("name", "email", "password1", "password2")

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not re.match("^[A-Za-z]*$", name):
            raise forms.ValidationError("Name must contain only letters.")
        return name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise forms.ValidationError("Enter a valid email address.")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists.")
        return email

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        errors = []
        if len(password1) < 8:
            errors.append("Password must be at least 8 characters long.")
        if not re.search(r'\d', password1):
            errors.append("Password must contain a number.")
        if not re.search(r'[A-Z]', password1):
            errors.append("Password must contain an uppercase letter.")
        if not re.search(r'\W', password1):
            errors.append("Password must contain a special character.")
        if errors:
            raise forms.ValidationError(errors)
        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['email']  # Set username as email
        if commit:
            user.save()
        return user
