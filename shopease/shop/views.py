from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'shop/index.html')

def about(request):
    return HttpResponse("About Page of Shop App")


def contact(request):
    return HttpResponse("Contact Page of Shop App")


def tracker(request):
    return HttpResponse("Tracker Page of Shop App")


def search(request):
    return HttpResponse("Search Page of Shop App")


def view_product(request):
    return HttpResponse("Product Details Page of Shop App")


def checkout(request):
    return HttpResponse("Checkout Page of Shop App")