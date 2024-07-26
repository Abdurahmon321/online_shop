from django.contrib.auth.models import User
from django.db import models
# Create your models here.


class RetailerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    status = models.BooleanField(default=False, null=True)
    firstname = models.CharField(max_length=50, null=True)
    lastname = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=100, null=True)
    phone_number = models.CharField(max_length=13, null=True)
    mobile_number = models.CharField(max_length=13, null=True)
    address = models.CharField(max_length=255, null=True)
    img = models.ImageField(upload_to="user_profile/", null=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
