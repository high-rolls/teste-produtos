from django.http import Http404, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Product

class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'

class ProductAjaxView(View):
    model = Product

    def get(self, request, *args, **kwargs):
        action = request.GET.get('action')

        if action == 'get':
            return self.get_product(request)
        
        raise Http404("Invalid action.")
    
    def post(self, request, *args, **kwargs):
        action = request.POST.get('action')

        if action == 'create':
            return self.create_product(request)
        elif action == 'update':
            return self.update_product(request)
        elif action == 'delete':
            return self.delete_product(request)
    
    def get_product(self, request):
        product_id = request.GET.get('id')
        product = get_object_or_404(Product, pk=product_id)

        data = {
            'id': product.id,
            'name': product.name,
            'description': product.description,
            'price': product.price
        }

        return JsonResponse(data)

    def create_product(self, request):
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')

        product = Product.objects.create(name=name, description=description, price=price)

        return JsonResponse({'success': True, 'id': product.id})

    def update_product(self, request):
        product_id = request.POST.get('productID')
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')

        product = Product.objects.get(pk=product_id)
        product.name = name
        product.description = description
        product.price = price
        product.save()
        print('X')

        return JsonResponse({'success': True, 'id': product.id})

    def delete_product(self, request):
        product_id = request.POST.get('productID')

        product = Product.objects.get(pk=product_id)
        product.delete()

        return JsonResponse({'success': True})