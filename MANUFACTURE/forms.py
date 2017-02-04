from django import forms
from django.contrib.auth.models import User
from .models import *
from django.utils.translation import ugettext_lazy as _



class Production_Order_Form(forms.ModelForm):

    class Meta:
        model = Production_Order
        fields = ['from_stock','to_stock']
        labels = { 'from_stock': _('من مخزن'),'to_stock':_('إلي مخزن')}

class Raw_Material_Form(forms.ModelForm):

    class Meta:
        model = Production_Raw_Material
        fields = ['amount']
        labels = {'amount':_('الكمية')}

class End_Products_Form(forms.ModelForm):

    class Meta:
        model = Production_Finished_Product
        fields = ['amount']
        labels = {'amount':_('الكمية')}