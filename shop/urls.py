from django.urls import path

from shop.views import ProductListView, ProductDetailView


app_name = 'shop'

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
]
