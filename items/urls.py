from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('products/cpu/', views.cpu, name= "cpu"),
    path('products/gpu/', views.gpu, name= "gpu"),
    path('products/motherboard/', views.mobo, name= "mobo"),
    path('products/memory/', views.memory, name= "memory"),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
]