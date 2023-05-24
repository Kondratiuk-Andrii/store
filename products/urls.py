from django.urls import path

from products.views import basket_add, basket_change, products

app_name = 'products'

urlpatterns = [
    path('', products, name='products'),
    path('page/<int:page>/', products, name='paginator'),
    path('<slug:category_slug>/', products, name='category'),
    path('<slug:category_slug>/page/<int:page>/', products, name='category_paginator'),
    path('basket/add/<int:product_id>/', basket_add, name='basket_add'),
    path('basket/change/<int:basket_id>/<str:operator>', basket_change, name='basket_change'),
]
