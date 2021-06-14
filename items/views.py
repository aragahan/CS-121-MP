from django.shortcuts import render
from django.views.generic.list import ListView
from django.http import JsonResponse
from .models import *
import json
# Create your views here.

def get_customer(user):
    if user.is_anonymous:
        guest_user = User.objects.get(username="guest") # or whatever ID or name you use for the placeholder user that no one will be assigned
        guest_author = Customer.objects.get_or_create(user=guest_user)
        return guest_author
    else:
        return Customer.objects.get(user=user) 
def home (request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        total = order.get_quantity_total
    else:
        items=[]
        order = {'get_cart_total':0, 'get_quantity_total':0}
        total = order['get_quantity_total']
    context={'total':total}
    return render(request, 'store/index.html', context)
def search(request):
    if request.method == 'GET':
        name = request.GET.get('search')
        try:
            status=Product.objects.filter(name__contains = name)
        except Product.DoesNotExist:
            status = None
        return render(request,"store/search.html",{"products":status,'name':name})
    else:
        return render(request,"store/search.html",{})

def cart(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        total = order.get_quantity_total
    else:
        items=[]
        order = {'get_cart_total':0, 'get_quantity_total':0}
        total = order['get_quantity_total']
    context = {"items":items, 'order':order,'total':total }
    return render(request, 'store/cart.html', context)

def about(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        total = order.get_quantity_total
    else:
        items=[]
        order = {'get_cart_total':0, 'get_quantity_total':0}
        total = order['get_quantity_total']
    context={'total': total}
    return render(request, 'store/about.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        total = order.get_quantity_total
    else:
        items=[]
        order = {'get_cart_total':0, 'get_quantity_total':0}
        total = order['get_quantity_total']
    context = {'total':total}
    return render(request, 'store/checkout.html', context)

def login(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        total = order.get_quantity_total
    else:
        items=[]
        order = {'get_cart_total':0, 'get_quantity_total':0}
        total = order['get_quantity_total']
    context = {'total':total}
    return render(request, 'store/login.html', context)

def register(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        total = order.get_quantity_total
    else:
        items=[]
        order = {'get_cart_total':0, 'get_quantity_total':0}
        total = order['get_quantity_total']
    context = {'total':total}
    return render(request, 'store/register.html', context)

def product(request,id):
    if request.user.is_authenticated:
        customer=request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        total = order.get_quantity_total
    else:
        items=[]
        order = {'get_cart_total':0, 'get_quantity_total':0}
        total = order['get_quantity_total']
    ratings = Rating.objects.all()
    product= Product.objects.get(id=id)
    context = {'product':product, 'total':total, 'ratings':ratings}
    return render(request,'store/product.html',context)

def cpu(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        total = order.get_quantity_total
    else:
        items=[]
        order = {'get_cart_total':0, 'get_quantity_total':0}
        total = order['get_quantity_total']
    products = Product.objects.filter(category=1)
    context = {'products': products, 'total':total}
    return render(request, 'store/products/components/cpu.html', context)

def mobo(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        total = order.get_quantity_total
    else:
        items=[]
        order = {'get_cart_total':0, 'get_quantity_total':0}
        total = order['get_quantity_total']
    products = Product.objects.filter(category__startswith='mobo')
    
    context = {'products': products,'total':total}
    return render(request, 'store/products/components/mobo.html', context)

def memory(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        total = order.get_quantity_total
    else:
        items=[]
        order = {'get_cart_total':0, 'get_quantity_total':0}
        total = order['get_quantity_total']
    products = Product.objects.filter(category__startswith='memory')
    context = {'products': products,'total':total}
    return render(request, 'store/products/components/memory.html', context)

def gpu(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        total = order.get_quantity_total
    else:
        items=[]
        order = {'get_cart_total':0, 'get_quantity_total':0}
        total = order['get_quantity_total']
    products = Product.objects.filter(category__startswith='gpu')
    context = {'products': products, 'total':total}
    return render(request, 'store/products/components/gpu.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data ['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)

    customer = request.user.customer
    product = Product.objects.get(id = productId)
    order, created = Order.objects.get_or_create(customer = customer, complete = False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    elif action == 'removeall':
        orderItem.quantity = 0
         
    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)