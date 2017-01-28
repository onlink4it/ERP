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
	def __str__(self):
		return self.user.username

class Treasury(models.Model):
	date = models.DateTimeField()
	amount = models.FloatField()
	comment = models.CharField(max_length = 128)

class System_Setting(models.Model):
	company_name = models.CharField(max_length = 64, default = "")
	company_logo = models.FileField()
	pos_from_stock = models.BooleanField(default = False)
