from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    brand = models.CharField(max_length=200, null=True)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.name


class CPU(Product):
    cores = models.FloatField()
    clockspeed = models.FloatField()
    graphics = models.CharField(max_length=200, null=True)


class GPU(Product):
    chipset = models.CharField(max_length=200, null=True)
    vram = models.FloatField()
    clockspeed = models.FloatField()


class Motherboard(Product):
    socket = models.CharField(max_length=200, null=True)
    formfactor = models.CharField(max_length=200, null=True)


class Memory(Product):
    memorytype = models.CharField(max_length=200, null=True)
    speed = models.FloatField()
    capacity = models.FloatField()


class Storage(Product):
    storagetype = models.CharField(max_length=200, null=True)
    capacity = models.FloatField()


class PSU(Product):
    capacity = models.FloatField()


class CPUCooler(Product):
    coolertype = models.CharField(max_length=200, null=True)
    rpm = models.FloatField()


class Monitor(Product):
    resolution = models.CharField(max_length=200, null=True)
    refreshrate = models.FloatField()


class Mouse(Product):
    dpi = models.FloatField()
    wireless = models.BooleanField()


class Keyboard(Product):
    switchtype = models.CharField(max_length=200, null=True)
    switch = models.CharField(max_length=200, null=True)


class Headset(Product):
    wireless = models.BooleanField()


class Case(Product):
    casetype = models.CharField(max_length=200, null=True)
    color = models.CharField(max_length=200, null=True)


class CaseAcc(Product):
    rpm = models.FloatField()
    size = models.FloatField()


class Rating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(
        1), MaxValueValidator(5)], blank=True, default=0)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_order = models.DateTimeField(auto_now_add=True)

    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    def get_quantity_total(self):
        orderquant = self.orderitem_set.all()
        quantots = sum(items.product.id for items in orderquant)
        return quantots


class OrderItem(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(
        Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class ShippingAddress(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(
        Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zip = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
