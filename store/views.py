from django.shortcuts import render
from .models import Product, Slider, Category
from django.core.paginator import Paginator

def index(request):
    products = Product.objects.select_related('author').filter(featured=True)
    slides = Slider.objects.order_by('order')
    return render(request, 'index.html', {'products': products, 'slides': slides})


def product(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'product.html', {'product': product})

def category(request, category_id=None):
    cat = None
    where = {}
    if category_id:
        cat = Category.objects.get(id=category_id)
        where['category_id'] = category_id
    products = Product.objects.filter(**where)
    paginator = Paginator(products, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'category.html',
                  {'category': cat, 
                   'page_obj': page_obj})

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')

def checkout_complete(request):
    return render(request, 'checkout-complete.html')