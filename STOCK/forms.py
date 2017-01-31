from django import forms
from django.contrib.auth.models import User
from .models import *
from django.utils.translation import ugettext_lazy as _



class Warehouse_Form(forms.ModelForm):
    class Meta:
        model = Warehouse
        fields = ['name','location']
        labels = { 'name': _('اسم المخزن'),'location': _('عنوان المخزن')}
        
class Warehouse_Transfer_Transaction_Form(forms.ModelForm):
    class Meta:
        model = Warehouse_Transfer_Transaction
        fields = ['from_warehouse','to_warehouse','item','quantity']
        labels = { 'from_warehouse': _('من مخزن'),'to_warehouse': _('الي مخزن'),'item': _('المنتج'),'quantity': _('الكمية')}


class Stock_Add_Form(forms.ModelForm):
    class Meta:
        model = Warehouse_Stock
        fields = ['warehouse','item','quantity']
        labels = { 'warehouse': _('المخزن'),'item': _('اسم المنتج'),'quantity': _('الكمية')}

class Stock_Search_Form(forms.ModelForm):
    class Meta:
        model = Warehouse_Stock
        fields = ['item']
        labels = { 'item': _('اسم المنتج')}

