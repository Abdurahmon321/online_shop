from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='category/')
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE, related_name="subcategory")
    slug = models.SlugField(unique=True, blank=True, null=True,)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    img1 = models.ImageField(upload_to="product/")
    img2 = models.ImageField(upload_to="product/", null=True, blank=True)
    img3 = models.ImageField(upload_to="product/", null=True, blank=True)
    img4 = models.ImageField(upload_to="product/", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=0)
    slug = models.SlugField(unique=True, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE, related_name="subcomment")

    def __str__(self):
        return f"{self.product}, {self.author}"


""" Cart ucuhun modellar """


class Cart(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    firstname = models.CharField(max_length=50, null=True)
    lastname = models.CharField(max_length=50, null=True)
    created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.author


class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="cart_products")
    quantity = models.IntegerField(default=0)
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product


""" baholash uchun model """


class Rate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.product.name}: {self.rating}"


""" chat uchun modell """


class Chat(models.Model):
    user1 = models.ForeignKey(User, related_name='user1_chats', on_delete=models.CASCADE)
    user2 = models.ForeignKey(User, related_name='user2_chats', on_delete=models.CASCADE)

    def __str__(self):
        return f"Chat between {self.user1} and {self.user2}"


class Message(models.Model):
    chat = models.ForeignKey(Chat, related_name="messages", on_delete=models.CASCADE)
    sender = models.ForeignKey(User, related_name="sent_messages", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return f"{self.sender}: {self.content}"


""" user profili uchun model """


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=13)
    mobile_number = models.CharField(max_length=13)
    address = models.CharField(max_length=255)
    img = models.ImageField(upload_to="user_profile/")

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


""" like va views uchun model """


class Like(models.Model):
    product = models.ForeignKey(Product, related_name='likes', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['product', 'user']

    def __str__(self):
        return f"{self.user.username} likes {self.product.name}"


class View(models.Model):
    product = models.ForeignKey(Product, related_name='views', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='views', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['product', 'user']

    def __str__(self):
        return f"{self.user.username} viewed {self.product.name}"


""" discount uchun model """


class Discount(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    discount_per = models.IntegerField(default=0)
    end_it = models.DateTimeField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product