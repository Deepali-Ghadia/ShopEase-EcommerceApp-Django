# This file is created by me

from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="shop_app_index"),
    path("about/", views.index, name="shop_app_about"),
    path("contact_us/", views.contact, name="shop_app_contact_us"),
    path("tracker/", views.tracker, name="shop_app_tracker"),
    path("search/", views.search, name="shop_app_search"),
    path("view_product/", views.view_product, name="shop_app_view_product"),
    path("checkout/", views.checkout, name="shop_app_checkout"),
    
]
