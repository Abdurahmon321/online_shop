from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .models import Category, Product, Discount


class CategoryForm(forms.Form):
    class Meta:
        model = Category
        fields = ['name', 'img', 'parent']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["category", "name", "img1", "img2", "img3", "img4", "price", "description", "quantity"]


class DiscountForm(forms.Form):
    class Meta:
        model = Discount
        fields = ["product", "discount_per", "end_it"]


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))


class UserSignupForm(UserCreationForm):
    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if len(password1) < 8:
            raise ValidationError(_('Parol kamida 8 ta belgidan iborat bo\'lishi kerak.'))
        return password1

    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "text",
        "placeholder": "enter username"
    }), label="Username")

    password1 = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "password",
        "placeholder": "enter password"
    }))
    password2 = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "password",
        "placeholder": "re-enter password"
    }))
