from django.shortcuts import render
from .models import Product, Category


def product_list(request):
    return render(request, 'catalog/products_list.html', {
        'products': Product.objects.all()
    })


def category(request, slug):
    category = Category.objects.get(slug=slug)
    return render(request, 'catalog/category.html', {
        'current_category': category,
        'product_list': Product.objects.filter(category=category)
    })


def product(request, slug):
    return render(request, 'catalog/product.html', {
        'product': Product.objects.get(slug=slug)
    })

