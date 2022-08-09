from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import ListView, View, DetailView, TemplateView, CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth.forms import UserCreationForm
from .models import *
import json

# Create your views here.
class BaseView(View):
       
    def get_context_data(self, **kwargs):
        if self.request.user.is_authenticated:
            customer, created = Customer.objects.get_or_create(user = self.request.user, name = self.request.user) 
            order, created = Order.objects.get_or_create(customer = customer, complete= False)
            items = order.orderitem_set.all()
            cartItems = order.cart_items
        else:
            customer={}
            items = []
            order = {'cart_total':0, 'cart_items':0}
            cartItems = order['cart_items']
        context = super().get_context_data(**kwargs)
        context['customer'] = customer
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

class OrderSummaryView(BaseView, ListView):
    model = OrderItem
    context_object_name = 'items'    
    template_name = 'UserApp/order_summary.html'

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
    
class UserLoginView(BaseView, LoginView):
    template_name = 'UserApp/user_login.html'
    next_page = reverse_lazy('store')


class UserLogoutView(BaseView, LogoutView):
    template_name = 'UserApp/user_logout.html'
    
class UserSignUpView(SuccessMessageMixin, BaseView,CreateView):
    template_name = 'UserApp/create_account.html'
    success_url = reverse_lazy('login')
    form_class = UserCreationForm
    success_message = "¡¡ Se creo tu perfil satisfactoriamente !!"
  
class UserUpdateView(BaseView , UpdateView):
    model = Customer
    fields = ['name', 'email']
    template_name_suffix = '_update'
    success_url = reverse_lazy('store')

class CheckoutFormView(BaseView, CreateView):
    model = ShippingInfo
    fields = ['address', 'city', 'state', 'zipcode']
    template_name = "UserApp/shipping_info.html"
    success_url = reverse_lazy('store')

    