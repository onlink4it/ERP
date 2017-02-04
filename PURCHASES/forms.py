from django import forms
from django.contrib.auth.models import User
from .models import *
from django.utils.translation import ugettext_lazy as _


class Purchase_Add_Invoice_Form(forms.ModelForm):
    class Meta:
        model = Purchase_Invoice
        fields = ['supplier']
        labels = { 'supplier': _('المورد')}

class Purchase_Invoice_Add_Item_Form(forms.ModelForm):
    class Meta:
        model = Purchase_Invoice_Item
        fields = ['item','quantity','unit_price']
        labels = { 'item': _('المنتج'),'quantity': _('الكمية'),'unit_price': _('سعر الوحدة')}

class Supplier_Form(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name','mobile','address','mail']
        labels = { 'name': _('الاسم'),'mobile': _('الموبايل'),'address': _('العنوان'),'mail': _('البريد الالكتروني')}

class Supplier_Transaction_Form(forms.ModelForm):
    class Meta:
        model = Supplier_Transaction
        fields = ['amount']
        labels = { 'amount': _('الكمية')}
