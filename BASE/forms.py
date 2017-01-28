from django import forms
from django.contrib.auth.models import User
from .models import *
from django.utils.translation import ugettext_lazy as _


class Item_Category_Form(forms.ModelForm):
    class Meta:
        model = Item_Category
        fields = ['name']

class Item_Form(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['category','name','price']
