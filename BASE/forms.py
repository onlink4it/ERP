from django import forms
from django.contrib.auth.models import User
from .models import *
from django.utils.translation import ugettext_lazy as _


class Item_Category_Form(forms.ModelForm):
    class Meta:
        model = Item_Category
        fields = ['name']
        labels = { 'name': _('اسم التصنيف')}

class Item_Form(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['category','name','price','stock_managed','add_to_website','raw_material','produced_item']
        labels = { 'category': _('التصنيف'),'name': _('اسم المنتج'),'price': _('السعر'),'stock_managed':_('إدارة المخزون لهذا المنتج'),
            'add_to_website':_('إضافة إلي الموقع'), 'raw_material':_('هذا المنتج مادة خام') , 'produced_item':_('هذا المنتج نقوم بتصنيعه')}

class Expense_Category_Form(forms.ModelForm):
    class Meta:
        model = Expense_Category
        fields = ['name']
        labels = { 'name': _('اسم التصنيف')}

class Expense_Transaction_Form(forms.ModelForm):
    class Meta:
        model = Expense_Transaction
        fields = ['category','amount','comment']
        labels = { 'category': _('التصنيف'),'amount': _('الكمية'),'comment': _('تعليق')}

class UserForm(forms.ModelForm):

    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username' ,'password','first_name','last_name','email']
        labels = { 'first_name': _('الاسم الاول'),'last_name': _('اسم العائلة'),'username': _('اسم المستخدم'),
                'password':_('كلمة السر'),'email':_('البريد الالكتروني '),}
class User_Admin_Form(forms.ModelForm):

    class Meta:
        model = User_Admin
        fields = ['is_pos_employee' ,'is_pos_admin','is_delivery_taker','is_delivery_admin','is_product_admin','is_invoice_admin','is_purchases_admin',
        'is_stock_admin','is_user_admin','is_accounts_admin','is_delivery_pilot']
        labels = { 'is_pos_employee': _('موظف كاشير'),'is_pos_admin': _('مدير كاشير'),'is_delivery_taker': _('دليفري تيكر'),
                'is_product_admin':_('مدير منتجات'),'is_invoice_admin':_('مدير الفواتير'),'is_purchases_admin':_('مدير مشتريات'),
                'is_stock_admin':_('مدير مخزون'),'is_user_admin':_('مدير حسابات الموظفين '),'is_accounts_admin':_("مدير حسابات"),
                'is_delivery_pilot':_('طيار دليفري'),'is_delivery_admin':_('مدير دليفري')}