from django.contrib import admin
from django.urls import path, include
from api import views

urlpatterns = [
    path('', views.product_list),
    path('api/products', views.product_list),
    path('api/product/<int:id>', views.product_description),
    path('api/categories', views.category_list),
    path('api/categories/<int:id>', views.category_by_id),
    path('api/categories/<int:id>/products', views.products_by_category)
]
