from django.db import models
from BASE.models import *
from django.contrib.auth.models import Permission, User
from datetime import datetime
# Create your models here.

class Branch(models.Model):
	name = models.CharField(max_length=64)
	address = models.CharField(max_length=512)
	phone = models.CharField(max_length = 16)
	def get_warehouse(self):
		branch_stock = Branch_Stock.objects.get(branch = self)
		warehouse = branch_stock.warehouse
		return warehouse
	def __str__(self):
		return self.name

class Branch_Stock(models.Model):
	branch = models.ForeignKey(Branch, on_delete = models.SET_NULL, null = True)
	warehouse = models.ForeignKey(Warehouse, on_delete = models.CASCADE)

class Branch_Users(models.Model):
	branch = models.ForeignKey(Branch, on_delete = models.CASCADE)
	user = models.ForeignKey(User, on_delete = models.CASCADE, unique = True)
	warehouse = models.ForeignKey(Warehouse, on_delete = models.CASCADE)