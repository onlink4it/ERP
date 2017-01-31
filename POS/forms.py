from django import forms
from django.contrib.auth.models import User
from .models import *
from django.utils.translation import ugettext_lazy as _


class POS_CustomerForm(forms.ModelForm):

    class Meta:
        model = POS_Customer
        fields = ['name']
        labels = { 'name': _('اسم العميل')}

class POS_Add_Invoice_Form(forms.ModelForm):
    class Meta:
        model = POS_Invoice
        fields = ['customer']
        labels = { 'customer': _('اسم العميل')}

class POS_Customer_Payment_Form(forms.ModelForm):
    class Meta:
        model = POS_Transactions
        fields = ['amount']
        labels = { 'amount': _('المبلغ')}

class POS_Employee_Payment_Form(forms.ModelForm):
    class Meta:
        model = Treasury
        fields = ['amount']
        labels = { 'amount': _('المبلغ')}