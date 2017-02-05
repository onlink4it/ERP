from django import forms
from django.contrib.auth.models import User
from BASE.models import *
from django.utils.translation import ugettext_lazy as _


class User_Form(forms.ModelForm):
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','password','first_name','last_name','email']
        labels = { 
        	'username': _('اليوزرنيم للمستخد الاساسي'),
        	'password': _('كلمة السر للمستخدم الاساسي'),
        	'first_name': _('الاسم الاول'),
        	'last_name': _('اسم العائلة'),
        	'email': _('الايميل'),
        }

class Admin_Form(forms.ModelForm):

    class Meta:
        model = User_Admin
        fields = ['is_pos_employee' ,'is_pos_admin','is_delivery_taker','is_delivery_admin','is_product_admin','is_invoice_admin','is_purchases_admin',
        'is_stock_admin','is_user_admin','is_accounts_admin','is_delivery_pilot']
        labels = { 'is_pos_employee': _('موظف كاشير'),'is_pos_admin': _('مدير كاشير'),'is_delivery_taker': _('دليفري تيكر'),
                'is_product_admin':_('مدير منتجات'),'is_invoice_admin':_('مدير الفواتير'),'is_purchases_admin':_('مدير مشتريات'),
                'is_stock_admin':_('مدير مخزون'),'is_user_admin':_('مدير حسابات الموظفين '),'is_accounts_admin':_("مدير حسابات"),
                'is_delivery_pilot':_('طيار دليفري'),'is_delivery_admin':_('مدير دليفري')}


class Branch_Form(forms.ModelForm):
    class Meta:
        model = Branch
        fields = ['name','address','phone']
        labels = { 'name': _('اسم الفرع'),'address': _('عنوان الفرع'),'phone':_('رقم التليفون')}


class System_Form(forms.ModelForm):
    class Meta:
        model = System_Setting
        fields = ['company_name','company_logo']
        labels = { 'company_name': _('اسم الشركة'),'company_logo': _('اللوجو')}
