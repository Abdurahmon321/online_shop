from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="admin_index"),

    path("retailers/", views.all_retailers, name="retailers"),
    path("add_retailer/", views.add_retailers, name="add_retailer"),
    path("delete_retailer/<int:pk>/", views.delete_retailers, name="delete_retailer"),

    path("users/", views.all_users, name="users"),
    path("delete_user/<int:pk>/", views.delete_user, name="delete_user"),

    path("categories/", views.all_categories, name="categories"),

    path("products/", views.all_products, name="products"),
    path("add_product/", views.add_product, name="add_product"),

    path("discounts/", views.all_discounts, name="discounts"),
]
