from django.shortcuts import redirect
from store.models import Cart, Product, Orders
from .forms import UserInfoForm



def make_order(request):
    if request.method != "POST":
        return redirect("store.checkout")
    
    form = UserInfoForm(request.POST)
    if form.is_valid():
        cart = Cart.objects.filter(session=request.session.session_key).last()
        products = Product.objects.filter(pk__in=cart.items)
        
        total = 0
        for item in products:
            total += item.price

        if total <= 0:
            return redirect("store.cart")
        

        order = Orders.objects.create(customer=form.cleaned_data, total=total)
        for product in products:
            order.orderitem_set.create(product_id=product.id, price=product.price)
        
        cart.delete()
        return redirect('store.checkout_complete')
    else:
        return redirect('store.checkout')