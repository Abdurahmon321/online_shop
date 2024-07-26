from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class AdminProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    status = models.BooleanField(default=False)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=13)
    mobile_number = models.CharField(max_length=13)
    address = models.CharField(max_length=255)
    img = models.ImageField(upload_to="user_profile/")

    def __str__(self):
        return f"{self.firstname} {self.lastname}"