from django.urls import path

from . import views

urlpatterns = [
    path('products/', views.get_products),
    path('products/<int:product_id>/', views.get_product),
    path('categories/', views.get_categories),
    path('categories/<int:category_id>/', views.get_category),
    path('categories/<int:category_id>/products/', views.get_category_products),
]