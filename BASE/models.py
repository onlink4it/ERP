from django.db import models
from django.contrib.auth.models import Permission, User


# Create your models here.
class Brand(models.Model):
	name = models.CharField(max_length = 64)

class Item_Category(models.Model):
	name = models.CharField(max_length = 64)
	def __str__(self):
		return self.name 

class Item(models.Model):
	category = models.ForeignKey(Item_Category, on_delete = models.CASCADE)
	name = models.CharField(max_length = 64)
	brand = models.ForeignKey(Brand, on_delete = models.CASCADE, default = 1,null = True, blank= True)
	price = models.FloatField(blank = True , null= True)
	pic = models.FileField(default = "")
	stock_managed = models.BooleanField(default = False)
	for_sale = models.BooleanField(default = False)
	raw_material = models.BooleanField(default = False)
	produced_item = models.BooleanField(default = False)
	critical_stock = models.FloatField(default = 0)
	add_to_website = models.BooleanField(default = False)
	def __str__(self):
		return self.category.name + " - " + self.name + " - " + str(self.price)


class User_Admin(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE,unique = True)
	mobile = models.CharField(max_length = 16,default = "")
	credit = models.FloatField(blank = True , null = True ,default = 0)

	is_pos_employee = models.BooleanField(default = False)
	is_pos_admin = models.BooleanField(default = False)

	is_delivery_taker = models.BooleanField(default = False)
	is_delivery_pilot = models.BooleanField(default = False)
	is_delivery_admin = models.BooleanField(default = False)

	is_accounts_admin = models.BooleanField(default = False)

	is_product_admin = models.BooleanField(default = False)
	is_invoice_admin = models.BooleanField(default = False)
	is_user_admin = models.BooleanField(default = False)
	is_superuser = models.BooleanField(default = False)

	is_stock_admin = models.BooleanField(default = False)

	is_purchases_admin = models.BooleanField(default = False)
	is_branches_admin = models.BooleanField(default = False)
	is_manufacture_admin = models.BooleanField(default = False)

	is_reports_admin = models.BooleanField(default = False)

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


class Warehouse(models.Model):
	name = models.CharField(max_length = 64)
	location = models.CharField(max_length = 512,null=True,blank= True)
	def __str__(self):
		return str(self.name) + " - " + str(self.location)

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