from django.shortcuts import render

# Create your views here.
from catalog.models import Category, Product


def index(request):
    return render(request, 'index.html', {
        'categories': Category.objects.all()
    })


def contact(request):
    return render(request, 'contact.html')
