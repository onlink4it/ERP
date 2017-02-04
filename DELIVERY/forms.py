from django import forms
from django.contrib.auth.models import User
from .models import *
from django.utils.translation import ugettext_lazy as _

class Delivery_InvoiceForm(forms.ModelForm):

    class Meta:
        model = Delivery_Invoice
        fields = ['customer','is_closed']

class Delivery_CustomerForm(forms.ModelForm):

    class Meta:
        model = Delivery_Customer
        fields = ['mobile']
        labels = { 'mobile': _('رقم الموبايل')}

class Delivery_Edit_CustomerForm(forms.ModelForm):
    class Meta:
        model = Delivery_Customer
        fields = ['address','mobile2','comment']
        labels = { 'address': _('العنوان'),'mobile2':_('موبايل آخر'), 'comment':_('ملاحظات')}

class Shipping_Form(forms.ModelForm):
    class Meta:
        model = Delivery_Invoice
        fields = ['shipped_with']