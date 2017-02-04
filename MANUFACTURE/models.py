from django.db import models
from BASE.models import *
from STOCK.models import *
from datetime import datetime
# Create your models here.
class Production_Order(models.Model):
	start_date = models.DateTimeField(null = True , blank = True)
	finish_date = models.DateTimeField(null = True , blank = True)
	is_started = models.BooleanField(default = False)
	is_finished = models.BooleanField(default = False)
	from_stock = models.ForeignKey(Warehouse, on_delete = models.CASCADE, related_name = "from_stock")
	to_stock = models.ForeignKey(Warehouse, on_delete = models.CASCADE, related_name = "to_stock", null = True, blank = True)
	def get_raw(self):
		return Production_Raw_Material.objects.filter(order = self.id)
	def get_end(self):
		return Production_Finished_Product.objects.filter(order = self.id)
	def __str__(self):
		return str(self.id)

class Production_Raw_Material(models.Model):
	order = models.ForeignKey(Production_Order, on_delete = models.CASCADE)
	item = models.ForeignKey(Item, on_delete = models.CASCADE)
	amount = models.FloatField()

class Production_Finished_Product(models.Model):
	order = models.ForeignKey(Production_Order, on_delete = models.CASCADE)
	item = models.ForeignKey(Item, on_delete = models.CASCADE)
	amount = models.FloatField()

