from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def index(request):
    products = Product.objects.all() # fetching products from the database
    # logic to create grids based on number of products
    no_of_products = len(products)
    params = {"products":products}
    return render(request, 'shop/index.html',params)

def about(request):
    return render(request,'shop/about.html')


def contact(request):
    return render(request,'shop/contact.html')


def tracker(request):
    return render(request,'shop/tracker.html')


def search(request):
    return render(request,'shop/search.html')


def view_product(request):
    return render(request,'shop/view_product.html')


def checkout(request):
    return render(request,'shop/checkout.html')