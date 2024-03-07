# This file is created by me

from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="shop_app_index"),
]
