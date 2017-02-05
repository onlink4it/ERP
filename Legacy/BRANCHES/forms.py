from django import forms
from django.contrib.auth.models import User
from .models import *
from django.utils.translation import ugettext_lazy as _

class Branch_Form(forms.ModelForm):
    class Meta:
        model = Branch
        fields = ['name','address','phone']
        labels = { 'name': _('اسم الفرع'),'address': _('عنوان الفرع'),'phone':_('رقم التليفون')}


class Choose_Branch_Form(forms.ModelForm):
    class Meta:
        model = Branch_Users
        fields = ['branch']
        labels = { 'branch': _('اسم الفرع')}