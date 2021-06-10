from django.shortcuts import render
from .models import *

# Create your views here.

def home (request):
    context = {}
    return render(request, 'store/index.html', context)

def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)

def login(request):
    context = {}
    return render(request, 'store/login.html', context)

def register(request):
    context = {}
    return render(request, 'store/register.html', context)

def cpu(request):
    products = Product.objects.filter(category__startswith='cpu')
    context = {'products': products}
    return render(request, 'store/products/components/cpu.html', context)

def mobo(request):
    products = Product.objects.filter(category__startswith='mobo')
    
    context = {'products': products}
    return render(request, 'store/products/components/mobo.html', context)

def memory(request):
    products = Product.objects.filter(category__startswith='memory')
    context = {'products': products}
    return render(request, 'store/products/components/memory.html', context)

def gpu(request):
    products = Product.objects.filter(category__startswith='gpu')
    context = {'products': products}
    return render(request, 'store/products/components/gpu.html', context)


