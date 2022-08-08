from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import ListView, View, DetailView, TemplateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
import json
from .models import *
# Create your views here.
class BaseView(View):
       
    def get_context_data(self, **kwargs):
        if self.request.user.is_authenticated:
            customer = self.request.user.customer
            order, created = Order.objects.get_or_create(customer = customer, complete= False)
            items = order.orderitem_set.all()
            cartItems = order.cart_items
        else:
            items = []
            order = {'cart_total':0, 'cart_items':0}
            cartItems = order['cart_items']
        context = super().get_context_data(**kwargs)
        context['order'] = order
        context['items'] = items
        context['cartItems'] = cartItems
        return context
    
class StoreView(BaseView, ListView):  
    queryset = Product.objects.all()
    context_object_name = 'products'
    template_name = 'UserApp/index.html'

class CartView(BaseView, ListView):
    model = OrderItem
    context_object_name = 'items'    
    template_name = 'UserApp/cart.html'


class CheckoutListItemView(BaseView, ListView):
    model = OrderItem
    context_object_name = 'items'    
    template_name = 'UserApp/checkout.html'


class ProductDetailView(BaseView, DetailView):
    model = Product
    context_object_name = 'product'

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    
    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer = customer, complete= False)
    
    orderItem, created = OrderItem.objects.get_or_create(order=order, product = product)
    
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    
    orderItem.save()
    
    if  orderItem.quantity <= 0:
        orderItem.delete()
    
    return JsonResponse('Item was addeded', safe=False)

class DeleteCartItem(BaseView, DeleteView):
    model = OrderItem
    success_url = reverse_lazy('cart')
    
class AboutView(BaseView, TemplateView):

    template_name = "UserApp/about_us.html"