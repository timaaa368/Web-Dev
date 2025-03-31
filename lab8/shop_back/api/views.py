from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from . import models

def get_products(request):
    products = models.Product.objects.all()
    products_json = [p.to_json() for p in products]

    return JsonResponse(products_json, safe=False)

def get_product(request, product_id):
    product = get_object_or_404(models.Product, pk=product_id)

    return JsonResponse(product.to_json())

def get_categories(request):
    categories = models.Category.objects.all()
    categories_json = [c.to_json() for c in categories]

    return JsonResponse(categories_json, safe=False)

def get_category(request, category_id):
    category = get_object_or_404(models.Category, pk=category_id)

    return JsonResponse(category.to_json())

def get_category_products(request, category_id):
    category_products = models.Category.objects.get(pk=category_id).product_set.all()
    category_products_json = [c.to_json() for c in category_products]

    return JsonResponse(category_products_json, safe=False)