from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from shop.models import Product
from .cart import Cart


@require_POST
def cart_add(request, product_slug):
    cart = Cart(request)
    product = get_object_or_404(Product, slug=product_slug)
    cart.add(product=product)
    return redirect('cart:cart_detail')


def cart_remove(request, product_slug):
    cart = Cart(request)
    product = get_object_or_404(Product, slug=product_slug)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})
