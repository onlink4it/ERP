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
        fields = ['is_pos_employee' ,'is_pos_admin','is_delivery_taker','is_delivery_pilot','is_delivery_admin','is_accounts_admin',
            'is_product_admin','is_invoice_admin','is_user_admin','is_superuser','is_stock_admin',
            'is_purchases_admin','is_branches_admin','is_manufacture_admin','is_reports_admin']
        labels = {
            'is_pos_employee':_('موظف كاشير') ,'is_pos_admin':_('مدير كاشير'),'is_delivery_taker':_('دليفري تيكر'),'is_delivery_pilot':_('طيار دليفري'),
            'is_delivery_admin':_('مدير دليفري'),'is_accounts_admin':_('إدارة الحسابات'),
            'is_product_admin':_('ادارة المنتجات'),'is_invoice_admin':_('ادارة الفاوتير'),
            'is_user_admin':_('ادارة الموظفين'),'is_superuser':_('مدير البرنامج'),'is_stock_admin':_('إدارة المخزون'),
            'is_purchases_admin':_('ادارة المشتريا'),'is_branches_admin':_('ادارة الفروع'),'is_manufacture_admin':_('دورات الانتاج'),
            'is_reports_admin':_('إدارة التقارير')
            }



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