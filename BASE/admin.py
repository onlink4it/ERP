from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Item_Category)
admin.site.register(Item)
admin.site.register(User_Admin)
admin.site.register(Treasury)
admin.site.register(Brand)
admin.site.register(Expense_Category)
admin.site.register(Expense_Transaction)
admin.site.register(System_Setting)
admin.site.register(Warehouse)
admin.site.register(Warehouse_Stock)
admin.site.register(Warehouse_Transfer_Transaction)
admin.site.register(Branch)
admin.site.register(Branch_Stock)
admin.site.register(Branch_Users)