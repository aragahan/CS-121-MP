from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(CPU)
admin.site.register(GPU)
admin.site.register(Motherboard)
admin.site.register(Memory)
admin.site.register(Storage)
admin.site.register(PSU)
admin.site.register(Monitor)
admin.site.register(Mouse)
admin.site.register(Keyboard)
admin.site.register(Headset)
admin.site.register(CaseAcc)
admin.site.register(Rating)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
