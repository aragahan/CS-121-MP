from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('about/', views.about, name="about"),
    path('update_item/', views.updateItem, name="update_item"),
    path('products/cpu/', views.cpu, name= "cpu"),
    path('products/gpu/', views.gpu, name= "gpu"),
    path('products/motherboard/', views.mobo, name= "mobo"),
    path('products/memory/', views.memory, name= "memory"),
    path('products/case/', views.case, name= "case"),
    path('products/psu/', views.psu, name= "psu"),
    path('products/caseaccessories/', views.caseacc, name= "caseacc"),
    path('products/headset/', views.headset, name= "headset"),
    path('products/keyboard/', views.keyboard, name= "keyboard"),
    path('products/monitor/', views.monitor, name= "monitor"),
    path('products/mouse/', views.mouse, name= "mouse"),
    path('products/<int:id>/',views.product, name='product'),
    path('search/',views.search, name='search'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
]