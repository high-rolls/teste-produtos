from django.urls import path
from .views import index_view, ProductListView, ProductAjaxView

urlpatterns = [
    path('', index_view),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/ajax/', ProductAjaxView.as_view(), name='product-ajax'),
]
