from django.db import models
from BASE.models import *
from django.contrib.auth.models import Permission, User
# Create your models here.

class Warehouse(models.Model):
	name = models.CharField(max_length = 64)
	location = models.CharField(max_length = 512,null=True,blank= True)
	def __str__(self):
		return self.name + self.location


class Warehouse_Stock(models.Model):
	warehouse = models.ForeignKey(Warehouse,on_delete=models.CASCADE)
	item = models.ForeignKey(Item,on_delete = models.CASCADE)
	quantity = models.IntegerField(blank = True , null = True , default = 0)
	def __str__(self):
		return self.warehouse.name + " - " + self.item.name + " - " + str(self.quantity)


class Warehouse_Transfer_Transaction(models.Model):
	from_warehouse = models.ForeignKey(Warehouse,on_delete=models.CASCADE,related_name="source")
	to_warehouse = models.ForeignKey(Warehouse,on_delete=models.CASCADE,related_name="target")
	item = models.ForeignKey(Item,on_delete = models.CASCADE)
	quantity = models.IntegerField(blank = True , null = True , default = 0)
	user = models.ForeignKey(User,on_delete=models.CASCADE,related_name = "sent_by")
	is_recieved = models.BooleanField(default = False)
	recieved_by = models.ForeignKey(User, null = True,on_delete = models.CASCADE, related_name = "recieved_by")
