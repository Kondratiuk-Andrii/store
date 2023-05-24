from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from products.models import Product, ProductCategory
from products.models import Basket


def index(request):
    context = {
        'title': 'Store',
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'Store - Каталог',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'products/products.html', context)


@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    basket = Basket.objects.filter(user=request.user, product=product)

    if not basket.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = basket.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_change(request, basket_id, operator):
    basket = Basket.objects.get(id=basket_id)
    # if operator:
    if operator == 'add':
        basket.quantity += 1
        basket.save()
    elif operator == 'subtract' and basket.quantity > 1:
        basket.quantity -= 1
        basket.save()
    elif operator == 'remove':
        basket.delete()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])
