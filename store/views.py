from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def product(request, product_id):
    return render(request, 'product.html')

def category(request, category_id=None):
    return render(request, 'category.html')

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')

def checkout_complete(request):
    return render(request, 'checkout-complete.html')