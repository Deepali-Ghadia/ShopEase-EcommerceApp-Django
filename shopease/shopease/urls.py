"""
URL configuration for shopease project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/',admin.site.urls),
    path("shop/", include('shop.urls')),
    path("blog/", include('blog.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# static(): This is a function provided by Django for serving static files during development. It takes two arguments:
# settings.MEDIA_URL: This is the URL prefix for serving media files. It's defined in the Django settings file (settings.py). For example, if MEDIA_URL is set to '/media/', then media files will be served under URLs starting with /media/.
# document_root=settings.MEDIA_ROOT: This specifies the directory from which to serve media files. It's also defined in the Django settings file (settings.py) as MEDIA_ROOT. This directory is typically where uploaded media files are stored on the server.

# whenever a django application is run, it first goes to this file (urls.py) {=> Reason ROOT_URLCONF = "shopease.urls"} and looks for the url to which request is made (shop/) in the urlpatterns array. When a match is found in the list, it understands that to get the further idea for the shop/ url, he needs to go to the urls file specified in the shop app directory.

# This way of structuring the url patters is beneficial because:
# If I have multiple urls of the shop app the url start with shop/ then django will get the path after shop/ from the shop.urls
# This way complete url paths of shop app are not disclosed in the urls.py of the main project.

# include ==> aage ki kahani for shop/ k liye go to shop.urls