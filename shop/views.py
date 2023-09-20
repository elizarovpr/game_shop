from django.shortcuts import render
from django.views.generic import ListView, DetailView

from shop.models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'index.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    slug_field = 'slug'
