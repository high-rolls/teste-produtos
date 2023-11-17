from django.urls import path
from .views import ProductListView, ProductAjaxView

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/ajax/', ProductAjaxView.as_view(), name='product-ajax'),
]
