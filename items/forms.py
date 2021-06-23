from django.forms import ModelForm, TextInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Order, ShippingAddress


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class AddressForm(ModelForm):
    class Meta:
        model = ShippingAddress
        fields = ['address', 'city', 'country', 'zip']
        widgets = {
            'address': TextInput(attrs={'placeholder': '1234 Main Street'}),
            'city': TextInput(attrs={'placeholder': 'Marikina City'}),
            'country': TextInput(attrs={'placeholder': 'Philippines'}),
            'zip': TextInput(attrs={'placeholder': '1810'}),
        }