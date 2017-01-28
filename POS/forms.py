from django import forms
from django.contrib.auth.models import User
from .models import *
from django.utils.translation import ugettext_lazy as _


class POS_CustomerForm(forms.ModelForm):

    class Meta:
        model = POS_Customer
        fields = ['name']

class POS_Add_Invoice_Form(forms.ModelForm):
    class Meta:
        model = POS_Invoice
        fields = ['customer']