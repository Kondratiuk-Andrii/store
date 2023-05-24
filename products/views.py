from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from products.models import Basket, Product, ProductCategory
from django.core.paginator import Paginator


def index(request):
    context = {
        'title': 'Store',
    }
    return render(request, 'products/index.html', context)


def products(request, category_slug=None, page=1):
    products = Product.objects.filter(category__slug=category_slug) if category_slug else Product.objects.all()

    per_page = 3
    paginator = Paginator(object_list=products, per_page=per_page)
    products_paginator = paginator.page(page)

    page_obj = paginator.get_page(page)

    context = {
        'title': 'Store - Каталог',
        'categories': ProductCategory.objects.all(),
        'category_slug': category_slug,
        'products': products_paginator,
        'page_obj': page_obj,
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
    if operator == 'add':
        basket.quantity += 1
        basket.save()
    elif operator == 'subtract' and basket.quantity > 1:
        basket.quantity -= 1
        basket.save()
    elif operator == 'remove':
        basket.delete()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])
