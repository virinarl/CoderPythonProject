from django.shortcuts import render
from .models import *
# Create your views here.
def store(request):
    products = Product.objects.all()
    context={'products':products}
    return render(request, 'UserApp/index.html',context)

def cart(request):
    return render(request, 'UserApp/cart.html',{})

def checkout(request):
    return render(request, 'UserApp/checkout.html',{})

