from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(POS_Customer)
admin.site.register(POS_Invoice)
admin.site.register(POS_Invoice_Items)
admin.site.register(POS_Transactions)