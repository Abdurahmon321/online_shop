from django import forms
from .models import RetailerProfile


class RetailerProfileForm(forms.Form):
    class Meta:
        model = RetailerProfile
        fields = ["status", "firstname", "lastname", "email", "phone_number", "mobile_number", "address", "img"]
