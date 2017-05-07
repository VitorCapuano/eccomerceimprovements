from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


def product_list(request):
    return render(request, 'products_list.html')


def product(request):
    return render(request, 'product.html')
