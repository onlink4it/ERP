from django.db import models
from django.contrib.auth.models import Permission, User


# Create your models here.
class Item_Category(models.Model):
	name = models.CharField(max_length = 64)
	def __str__(self):
		return self.name 

class Item(models.Model):
	category = models.ForeignKey(Item_Category, on_delete = models.CASCADE)
	name = models.CharField(max_length = 64)
	price = models.FloatField(blank = True , null= True)
	def __str__(self):
		return self.category.name + " - " + self.name + " - " + str(self.price)

class User_Admin(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE,unique = True)
	credit = models.FloatField(blank = True , null = True ,default = 0)
	#0
	is_pos_employee = models.BooleanField(default = False)
	#1
	is_pos_admin = models.BooleanField(default = False)
	#2
	is_delivery_taker = models.BooleanField(default = False)
	#3
	is_delivery_admin = models.BooleanField(default = False)
	#4
	is_product_admin = models.BooleanField(default = False)
	#5
	is_invoice_admin = models.BooleanField(default = False) 
	#6
	is_purchases_admin = models.BooleanField(default = False)
	#7
	is_stock_admin = models.BooleanField(default = False)
	#8
	is_user_admin = models.BooleanField(default = False)
	#9
	is_accounts_admin = models.BooleanField(default = False)
	is_superuser = models.BooleanField(default = False)
	def __str__(self):
		return self.user.username

class Treasury(models.Model):
	date = models.DateTimeField()
	amount = models.FloatField()
	comment = models.CharField(max_length = 128)

class Expense_Category(models.Model):
	name = models.CharField(max_length = 64)
	def __str__(self):
		return self.name

class Expense_Transaction(models.Model):
	date = models.DateTimeField()
	amount = models.FloatField()
	category = models.ForeignKey(Expense_Category, on_delete = models.CASCADE)
	comment = models.CharField(max_length = 256, null = True , blank = True)

class System_Setting(models.Model):
	company_name = models.CharField(max_length = 64, default = "")
	company_logo = models.FileField()
	pos_from_stock = models.BooleanField(default = False)
