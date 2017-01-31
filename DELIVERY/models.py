from django.db import models
from BASE.models import *
# Create your models here.

class Delivery_Customer(models.Model):
	mobile = models.CharField(max_length=16)
	address = models.CharField(max_length=512)
	def __str__(self):
		return str(self.mobile) + " - " + str(self.address)

class Delivery_Invoice(models.Model):
	customer = models.ForeignKey(Delivery_Customer,on_delete=models.CASCADE)
	date = models.DateTimeField()
	total_price = models.FloatField()
	is_closed = models.BooleanField(default=False)
	def get_items(self):
		return Delivery_Invoice_Items.objects.filter(invoice_id = self.id)

class Delivery_Invoice_Items(models.Model):
	invoice_id = models.ForeignKey(Delivery_Invoice,on_delete=models.CASCADE)
	item = models.ForeignKey(Item,on_delete =models.CASCADE)
	quantity = models.FloatField()
	unit_price = models.FloatField()
	total_price = models.FloatField()

class Delivery_Transactions(models.Model):
	date = models.DateTimeField(null = True , blank = True)
	customer = models.ForeignKey(Delivery_Customer, on_delete = models.CASCADE)
	amount = models.FloatField()
	paid_to = models.ForeignKey(User, on_delete = models.CASCADE,default = 1)
	def __str__(self):
		return self.customer.name + str(self.amount)