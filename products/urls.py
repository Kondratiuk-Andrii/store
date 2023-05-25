from django.urls import path

from products.views import ProductsListView, basket_add, basket_change

app_name = 'products'

urlpatterns = [
    path('', ProductsListView.as_view(), name='products'),
    path('page/<int:page>/', ProductsListView.as_view(), name='paginator'),
    path('<slug:category_slug>/', ProductsListView.as_view(), name='category'),
    path('<slug:category_slug>/page/<int:page>/', ProductsListView.as_view(), name='category_paginator'),

    path('basket/add/<int:product_id>/', basket_add, name='basket_add'),
    path('basket/change/<int:basket_id>/<str:operator>', basket_change, name='basket_change'),
]
