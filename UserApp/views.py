from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def store(request):
    return render(request, 'UserApp/index.html',{})

def cart(request):
    return render(request, 'UserApp/cart.html',{})

def checkout(request):
    return render(request, 'UserApp/checkout.html',{})

