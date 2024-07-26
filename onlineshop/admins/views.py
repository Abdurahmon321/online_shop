from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from shop.models import Product, Category, UserProfile
from retailer.models import RetailerProfile
from retailer.forms import RetailerProfileForm
from shop.forms import UserSignupForm, ProductForm


# Create your views here.


def index(request):
    context = {
        "total_retailers": RetailerProfile.objects.count(),
        "total_users": UserProfile.objects.count(),
        "total_products": Product.objects.count(),
        "total_categories": Category.objects.count()
    }
    return render(request, "admin/admin_dashboard.html", context)


""" admin retailer funksiyalari """


def all_retailers(request):
    return render(request, 'admin/retailer/retailers.html')


def add_retailers(request):
    if request.method == "POST":
        form = UserSignupForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            retailer = RetailerProfile.objects.create(user=user, status=True)
            return redirect("admin_index")
    else:
        form = UserSignupForm()
    return render(request, "admin/retailer/add_retailer.html", {"form": form})


def delete_retailers(request, pk):
    user = User.objects.get(id=pk)
    retailer_profile = RetailerProfile.objects.get(user_id=pk)
    if request.method == "POST":
        user.delete()
        retailer_profile.delete()
        return redirect("admin_index")
    return render(request, "admin/delete/delete_retailer_confirm.html", {"retailer_profile": retailer_profile})


""" admin user funksiyalari """


def all_users(request):
    return render(request, "admin/user/users.html")


def delete_user(request, pk):
    user = User.objects.get(id=pk)
    user_profile = UserProfile.objects.get(user_id=pk)
    if request.method == "POST":
        user.delete()
        user_profile.delete()
        return redirect("admin_index")
    return render(request, "admin/delete/delete_user_conf.html", {"user_profile": user_profile})


def detail_user(request):
    pass

""" admin categories funk """


def all_categories(request):
    return render(request, "admin/category/categories.html")

def add_category(request):
    pass

def update_category(request):
    pass

def delete_category(request):
    pass

def detail_category(request):
    pass

""" admin products """


def all_products(request):
    return render(request, "admin/product/products.html")


def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("admin_index")
    else:
        form = ProductForm()
    return render(request, "admin/product/add_product.html", {"form": form})


def update_product(request):
    pass

def delete_product(request):
    pass

def detail_product(request):
    pass



""" admin discount """


def all_discounts(request):
    return render(request, "admin/discount/discounts.html")

def add_discount(request):
    pass

def update_discount(request):
    pass

def delete_discount(request):
    pass