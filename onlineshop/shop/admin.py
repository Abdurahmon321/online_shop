from django.contrib import admin
from .models import (Category, Cart, CartProduct, Product, Comment,
                     Rate, Chat, Message, UserProfile, Like, View, Discount)
# Register your models here.
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(CartProduct)
admin.site.register(Product)
admin.site.register(Comment)
admin.site.register(Rate)
admin.site.register(Chat)
admin.site.register(Message)
admin.site.register(UserProfile)
admin.site.register(Like)
admin.site.register(View)
admin.site.register(Discount)
