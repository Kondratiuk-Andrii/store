from django.urls import path

from products.views import products, basket_add, basket_change

app_name = 'products'

urlpatterns = [
    path('', products, name='products'),
    path('category/<int:category_id>/', products, name='category'),
    path('basket/add/<int:product_id>/', basket_add, name='basket_add'),
    path('basket/change/<int:basket_id>/<str:operator>', basket_change, name='basket_change'),
]
