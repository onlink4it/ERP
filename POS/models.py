from django.db import models
from django.contrib.auth.models import Permission, User
from BASE.models import *

# Create your models here.
class POS_Customer(models.Model):
	name = models.CharField(max_length = 64)
	credit = models.FloatField(blank = True,default = 0)
	def __str__(self):
		return self.name 

class POS_Invoice(models.Model):
	date = models.DateTimeField()
	customer = models.ForeignKey(POS_Customer, on_delete  = models.CASCADE)
	is_closed = models.BooleanField(default = False)

	def __str__(self):
		return str(self.id) + " - " + str(self.date) + " - " + str(self.customer.name)

	def get_items(self):
		return POS_Invoice_Items.objects.filter(invoice_id = self.id)

class POS_Invoice_Items(models.Model):
	invoice = models.ForeignKey(POS_Invoice, on_delete = models.CASCADE)
	branch = models.ForeignKey(Branch, on_delete = models.CASCADE)
	item = models.ForeignKey(Item, on_delete = models.CASCADE)
	quantity = models.IntegerField()
	unit_price = models.FloatField()
	total_price = models.FloatField(default = 0)
	
	def __str__(self):
		return str(self.invoice.id) + " - " + str(self.item.name) + " - " + str(self.quantity) + " - " + str(self.unit_price)

	def total(self):
		return self.quantity * self.unit_price

class POS_Transactions(models.Model):
	date = models.DateTimeField(null = True , blank = True)
	customer = models.ForeignKey(POS_Customer, on_delete = models.CASCADE)
	amount = models.FloatField()
	paid_to = models.ForeignKey(User, on_delete = models.CASCADE,default = 1)
	def __str__(self):
		return self.customer.name + str(self.amount)