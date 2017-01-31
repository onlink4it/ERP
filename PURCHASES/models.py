from BASE.models import *

# Create your models here.

class Supplier(models.Model):
	name = models.CharField(max_length= 64)
	mobile = models.CharField(max_length=16,null=True,blank=True)
	address = models.CharField(max_length = 256,null=True,blank=True)
	mail = models.CharField(max_length = 128,null=True,blank=True)
	credit = models.FloatField(null = True,blank = True,default=0)
	def __str__(self):
		return self.name

class Purchase_Invoice(models.Model):
	date = models.DateTimeField()
	supplier = models.ForeignKey(Supplier,on_delete = models.CASCADE)
	total_price = models.FloatField(null=True,blank=True,default=0)
	delivered = models.BooleanField(default=False)
	def __str__(self):
		return str(self.date) + " - " + self.supplier.name + " - " + str(self.total_price)

	def get_items(self):
		return Purchase_Invoice_Item.objects.filter(invoice_id = self.id)

class Purchase_Invoice_Item(models.Model):
	invoice_id = models.ForeignKey(Purchase_Invoice,on_delete = models.CASCADE)
	item = models.ForeignKey(Item , on_delete=models.CASCADE)
	quantity = models.FloatField()
	unit_price = models.FloatField()
	total_price = models.FloatField()

class Supplier_Transaction(models.Model):
	date = models.DateTimeField()
	supplier = models.ForeignKey(Supplier,on_delete = models.CASCADE)
	amount = models.FloatField()
	comment = models.CharField(max_length=512)
