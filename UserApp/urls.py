from django.urls import path
from . import views


urlpatterns = [
    path('', views.StoreView.as_view(), name = 'store'),
    path('cart/', views.CartView.as_view(), name = 'cart'),
    path('checkout/', views.CheckoutListItemView.as_view(), name = 'checkout'),
    path('product/<pk>/', views.ProductDetailView.as_view(), name = 'productDetail'),
    path('item/<pk>', views.DeleteCartItem.as_view(), name = 'deleteItem'),
    path('update_item/', views.updateItem, name = 'updateItem'),
    path('about_us/', views.AboutView.as_view(), name = 'about'),
    path('login/', views.UserLoginView.as_view(), name = 'login'),
    path('logout/', views.UserLogoutView.as_view(), name = 'logout'),
    path('singup/', views.UserSignUpView.as_view(), name = 'singup')
]
