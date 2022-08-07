from django.urls import path
from . import views

urlpatterns = [
    path('', views.StoreView.as_view(), name='store'),
    path('cart/', views.CartView.as_view(), name='cart'),
    path('checkout/', views.CheckoutListItemView.as_view(), name='checkout'),
    
    path('update_item/', views.updateItem, name='updateItem')
]
