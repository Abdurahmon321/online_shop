from django import template
from shop.models import UserProfile, Product, Category, Discount
from retailer.models import RetailerProfile
register = template.Library()


@register.simple_tag
def all_users():
    return UserProfile.objects.all()


@register.simple_tag
def all_retailers():
    return RetailerProfile.objects.all()


@register.simple_tag
def all_products():
    return Product.objects.all()


@register.simple_tag
def all_categories():
    return Category.objects.all()


@register.simple_tag
def all_discounts():
    return Discount.objects.all()
