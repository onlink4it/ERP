from django.contrib.auth import authenticate, login, logout
from django.template import loader
from datetime import date,datetime
from django.urls import reverse
from django import forms
from .models import *
from BASE.models import *
from STOCK.models import *
from .forms import *
from django.shortcuts import render,get_object_or_404,redirect

# Create your views here.

def purchase_home(request):
	if not request.user.is_authenticated():
		return render(request,'BASE/login.html')
	else:
		return render(request,"PURCHASES/purchase_home.html")

def purchase_supplier(request):
	if not request.user.is_authenticated():
		return render(request,'BASE/login.html')
	else:
		all_suppliers = Supplier.objects.all()
		form = Supplier_Form(request.POST or None)
		if form.is_valid():
			supplier = form.save(commit=False)
			supplier.save()
			context = {"form":form,"all_suppliers":all_suppliers}
			return render(request,'PURCHASES/purchase_supplier.html',context)
		context = {"form":form,"all_suppliers":all_suppliers}
		return render(request,'PURCHASES/purchase_supplier.html',context)	

def purchase_supplier_payment(request,supplier_id):
	if not request.user.is_authenticated():
		return render(request,'BASE/login.html')
	else:

		supplier = Supplier.objects.get(pk = supplier_id)
		all_suppliers_trans = Supplier_Transaction.objects.filter(supplier=supplier)
		form = Supplier_Transaction_Form(request.POST or None)
		if form.is_valid():
			trans = form.save(commit = False)
			trans.date = datetime.now()
			trans.supplier = supplier
			trans.comment = "سداد"
			trans.save()
			supplier.credit -= trans.amount
			treasury_trans = Treasury()
			treasury_trans.date = datetime.now()
			treasury_trans.amount = -trans.amount
			treasury_trans.comment = "سداد حساب المورد" + supplier.name
			treasury_trans.save()
			supplier.save()
			return redirect('../../')
		context = {'form':form , 'supplier':supplier,'all_suppliers_trans':all_suppliers_trans}
		return render(request,'PURCHASES/purchase_supplier_payment.html',context)


def purchase_add_invoice(request):
	if not request.user.is_authenticated():
		return render(request, 'BASE/login.html')
	else:
		all_invoices = Purchase_Invoice.objects.all()
		all_suppliers = Supplier.objects.all()
		form = Purchase_Add_Invoice_Form(request.POST or None)
		if form.is_valid():
			x = form.save(commit=False)
			x.date = datetime.now()
			x.save()
			return redirect('../Invoice/' + str(x.id) , inv_id = x.id)
		context = {"form":form,"all_invoices":all_invoices,"all_suppliers":all_suppliers}
		return render(request,'PURCHASES/purchase_invoice.html',context)

def purchase_invoice_item(request,inv_id):
	if not request.user.is_authenticated():
		return render(request, 'BASE/login.html')
	else:
		all_items = Purchase_Invoice_Item.objects.all()
		inv_items = Purchase_Invoice_Item.objects.filter(invoice_id = inv_id)
		this_inv = Purchase_Invoice.objects.get(pk=inv_id)
		all_warehouses = Warehouse.objects.all()
		form = Purchase_Invoice_Add_Item_Form(request.POST or None)
		if form.is_valid():
			x = form.save(commit=False)
			x.invoice_id = this_inv
			x.total_price = x.quantity * x.unit_price
			x.save()
			return redirect('../' + str(inv_id), inv_id = inv_id)
		context = {"form":form,"all_items":all_items,"inv_items":inv_items,"this_inv":this_inv,'all_warehouses':all_warehouses}
		return render(request,'PURCHASES/purchase_items.html',context)	


def purchase_invoice_delivered(request,inv_id):
	if not request.user.is_authenticated():
		return render(request, 'BASE/login.html')
	else:
		this_inv = Purchase_Invoice.objects.get(pk=inv_id)
		inv_items = Purchase_Invoice_Item.objects.filter(invoice_id = inv_id)
		all_warehouses = Warehouse.objects.all()
		inv_total = 0
		if request.method == "POST":
			for x in inv_items:
				inv_total += x.total_price
				try:
					warehouse_item = Warehouse_Stock.objects.get(warehouse=request.POST.get('warehouse') , item = x.item)
					warehouse_item.quantity += x.quantity
					warehouse_item.save()
					error_message = "تم إضافة الكمية"
				except Warehouse_Stock.DoesNotExist:
					this_warehouse = Warehouse.objects.get(pk = request.POST.get('warehouse') )
					warehouse_new_item = Warehouse_Stock()
					warehouse_new_item.item = x.item
					warehouse_new_item.warehouse =this_warehouse
					warehouse_new_item.quantity = x.quantity
					warehouse_new_item.save()
					error_message = "تم إضافة الصنف الي المخزن"
			this_inv.total_price  = inv_total
			this_inv.delivered = True
			supplier = Supplier.objects.get(pk=this_inv.supplier.id)
			supplier.credit += inv_total
			supplier.save()
			this_inv.save()
			context = {'error_message' : error_message,'inv_items':inv_items,'this_inv':this_inv}
			return render(request,'PURCHASES/purchase_items.html',context)
		else:
			error_message = "حدث خطأ ما"
			context = {'error_message' : error_message,'inv_items':inv_items,'this_inv':this_inv}
			return render(request,'PURCHASES/purchase_items.html',context)

def purchase_item_delete(request,inv_id,item_id):
	if not request.user.is_authenticated():
		return render(request, 'BASE/login.html')
	else:
		this_item = Purchase_Invoice_Item.objects.get(pk=item_id)
		this_item.delete()
		return redirect('../../')

def purchase_print_invoice(request,inv_id):
	if not request.user.is_authenticated():
		return render(request,'BASE/login.html')
	else:
		this_inv = Purchase_Invoice.objects.get(id=inv_id)
		inv_items = Purchase_Invoice_Item.objects.filter(invoice_id=inv_id)
		inv_total = 0
		for x in inv_items:
			inv_total += x.total_price
		context = {"this_inv":this_inv,"inv_items":inv_items,"inv_total":inv_total}
		return render(request, 'BASE/invoice.html',context)
