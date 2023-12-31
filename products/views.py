from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.views.generic.base import TemplateView

from common.views import CommonMixin
from products.models import Basket, Product, ProductCategory


class IndexView(CommonMixin, TemplateView):
    template_name = 'products/index.html'
    title = 'Store'


class ProductsListView(CommonMixin, ListView):
    model = Product
    template_name = 'products/products.html'
    paginate_by = 3
    title = 'Store - Каталог'

    def get_queryset(self):
        queryset = super(ProductsListView, self).get_queryset()
        category_slug = self.kwargs.get('category_slug')
        return queryset.filter(category__slug=category_slug) if category_slug else queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = cache.get('categories')
        if not categories:
            context['categories'] = ProductCategory.objects.all()
            cache.set('categories', context['categories'], 30)
        else:
            context['categories'] = categories
        context['category_slug'] = self.kwargs.get('category_slug')
        return context


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
