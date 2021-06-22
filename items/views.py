from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import CreateUserForm
from .decorators import unauthenticated_user
import json
# Create your views here.


def get_customer(user):
    if user.is_anonymous:
        # or whatever ID or name you use for the placeholder user that no one will be assigned
        guest_user = User.objects.get(username="guest")
        guest_author = Customer.objects.get_or_create(user=guest_user)
        return guest_author
    else:
        return Customer.objects.get(user=user)


def home(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        total = order.get_quantity_total
    else:
        items = []
        order = {'get_cart_total': 0, 'get_quantity_total': 0}
        total = order['get_quantity_total']
    context = {'total': total}
    return render(request, 'store/index.html', context)


def search(request):
    if request.method == 'GET':
        name = request.GET.get('search')
        try:
            status = Product.objects.filter(name__contains=name)
        except Product.DoesNotExist:
            status = None
        return render(request, "store/search.html", {"products": status, 'name': name})
    else:
        return render(request, "store/search.html", {})


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        total = order.get_quantity_total
    else:
        items = []
        order = {'get_cart_total': 0, 'get_quantity_total': 0}
        total = order['get_quantity_total']
    context = {"items": items, 'order': order, 'total': total}
    return render(request, 'store/cart.html', context)


def about(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        total = order.get_quantity_total
    else:
        items = []
        order = {'get_cart_total': 0, 'get_quantity_total': 0}
        total = order['get_quantity_total']
    context = {'total': total}
    return render(request, 'store/about.html', context)


def checkout(request):
    if request.user.is_authenticated:
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        address1 = request.POST.get('address1')
        address2 = request.POST.get('address2')
        country = request.POST.get('country')
        city = request.POST.get('city')
        postcode = request.POST.get('postcode')

        if (forms.selected("credit")): #only for credit card option
            cardname = request.POST.get('card-name')
            cardno = request.POST.get('card-no')
            expiry = request.POST.get('expiry')
            secno = request.POST.get('sec-no')
    else:
        return redirect('login')
    context = {}
    return render(request, 'store/checkout.html', context)


@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Username or Password is incorrect.")
            return redirect('login')

    context = {}
    return render(request, 'store/login.html', context)


def logUserOut(request):
    logout(request)
    return redirect('login')


@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            Customer.objects.create(
                user=user,
                name=form.cleaned_data.get('username'),
            )

            messages.success(request, 'Account creation success.')

            return redirect('login')

    context = {'form': form}
    return render(request, 'store/register.html', context)


def product(request, id):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        total = order.get_quantity_total
    else:
        items = []
        order = {'get_cart_total': 0, 'get_quantity_total': 0}
        total = order['get_quantity_total']
    ratings = Rating.objects.all()
    product = Product.objects.get(id=id)
    context = {'product': product, 'total': total, 'ratings': ratings}
    return render(request, 'store/product.html', context)


def cpu(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        total = order.get_quantity_total
    else:
        items = []
        order = {'get_cart_total': 0, 'get_quantity_total': 0}
        total = order['get_quantity_total']
    products = Product.objects.filter(category=1)
    context = {'products': products, 'total': total}
    return render(request, 'store/products/components/cpu.html', context)


def gpu(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        total = order.get_quantity_total
    else:
        items = []
        order = {'get_cart_total': 0, 'get_quantity_total': 0}
        total = order['get_quantity_total']
    products = Product.objects.filter(category=2)
    context = {'products': products, 'total': total}
    return render(request, 'store/products/components/gpu.html', context)


def mobo(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        total = order.get_quantity_total
    else:
        items = []
        order = {'get_cart_total': 0, 'get_quantity_total': 0}
        total = order['get_quantity_total']
    products = Product.objects.filter(category=3)

    context = {'products': products, 'total': total}
    return render(request, 'store/products/components/mobo.html', context)


def memory(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        total = order.get_quantity_total
    else:
        items = []
        order = {'get_cart_total': 0, 'get_quantity_total': 0}
        total = order['get_quantity_total']
    products = Product.objects.filter(category=4)
    context = {'products': products, 'total': total}
    return render(request, 'store/products/components/memory.html', context)


def case(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        total = order.get_quantity_total
    else:
        items = []
        order = {'get_cart_total': 0, 'get_quantity_total': 0}
        total = order['get_quantity_total']
    products = Product.objects.filter(category=5)
    context = {'products': products, 'total': total}
    return render(request, 'store/products/components/gpu.html', context)


def psu(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        total = order.get_quantity_total
    else:
        items = []
        order = {'get_cart_total': 0, 'get_quantity_total': 0}
        total = order['get_quantity_total']
    products = Product.objects.filter(category=6)
    context = {'products': products, 'total': total}
    return render(request, 'store/products/components/gpu.html', context)


def caseacc(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        total = order.get_quantity_total
    else:
        items = []
        order = {'get_cart_total': 0, 'get_quantity_total': 0}
        total = order['get_quantity_total']
    products = Product.objects.filter(category=7)
    context = {'products': products, 'total': total}
    return render(request, 'store/products/components/gpu.html', context)


def headset(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        total = order.get_quantity_total
    else:
        items = []
        order = {'get_cart_total': 0, 'get_quantity_total': 0}
        total = order['get_quantity_total']
    products = Product.objects.filter(category=8)
    context = {'products': products, 'total': total}
    return render(request, 'store/products/components/gpu.html', context)


def keyboard(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        total = order.get_quantity_total
    else:
        items = []
        order = {'get_cart_total': 0, 'get_quantity_total': 0}
        total = order['get_quantity_total']
    products = Product.objects.filter(category=9)
    context = {'products': products, 'total': total}
    return render(request, 'store/products/components/gpu.html', context)


def monitor(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        total = order.get_quantity_total
    else:
        items = []
        order = {'get_cart_total': 0, 'get_quantity_total': 0}
        total = order['get_quantity_total']
    products = Product.objects.filter(category=10)
    context = {'products': products, 'total': total}
    return render(request, 'store/products/components/gpu.html', context)


def mouse(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        total = order.get_quantity_total
    else:
        items = []
        order = {'get_cart_total': 0, 'get_quantity_total': 0}
        total = order['get_quantity_total']
    products = Product.objects.filter(category=11)
    context = {'products': products, 'total': total}
    return render(request, 'store/products/components/gpu.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(
        customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(
        order=order, product=product)

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
