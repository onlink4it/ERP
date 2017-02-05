from django.contrib.auth import authenticate, login, logout
from django.template import loader
from datetime import date,datetime
from django.urls import reverse
from django import forms
from .models import *
from BASE.models import *
from .forms import *
from django.shortcuts import render,get_object_or_404,redirect
# Create your views here.

def perm(request,x,permission):
	employee = User_Admin.objects.get(user = x)

	if permission == "is_pos_employee":
		if employee.is_pos_employee == True:
			return True
		else:
			return False
	if permission == "is_pos_admin":
		if employee.is_pos_admin == True:
			return True
		else:
			return False
	if permission == "is_delivery_taker":
		if employee.is_delivery_taker == True:
			return True
		else:
			return False
	if permission == "is_delivery_admin":
		if employee.is_delivery_admin == True:
			return True
		else:
			return False
	if permission == "is_product_admin":
		if employee.is_product_admin == True:
			return True
		else:
			return False
	if permission == "is_invoice_admin":
		if employee.is_invoice_admin == True:
			return True
		else:
			return False
	if permission == "is_purchases_admin":
		if employee.is_purchases_admin == True:
			return True
		else:
			return False
	if permission == "is_stock_admin":
		if employee.is_stock_admin == True:
			return True
		else:
			return False
	if permission == "is_user_admin":
		if employee.is_user_admin == True:
			return True
		else:
			return False
	if permission == "is_accounts_admin":
		if employee.is_accounts_admin == True:
			return True
		else:
			return False

def Delivery_home(request):
	if not request.user.is_authenticated():
		return render(request,'BASE/login.html')
	else:
		if perm(request,request.user,"is_delivery_taker") == True or perm(request,request.user,"is_delivery_admin") == True:
			all_invoices = Delivery_Invoice.objects.all()
			opened_inv = Delivery_Invoice.objects.filter(is_closed=False)
			form = Delivery_CustomerForm(request.POST or None)
			if form.is_valid():
				mob = form.save(commit = False)
				try:
					this_customer = Delivery_Customer.objects.filter(mobile=mob.mobile)[:1].get()
					customer_address = Delivery_Customer.objects.filter(mobile = mob.mobile)
					customer_invoices = Delivery_Invoice.objects.filter(customer__mobile = mob.mobile)
					context = {'customer_address':customer_address,'all_invoices':all_invoices,"customer_invoices":customer_invoices}
					return render(request,'Delivery/delivery_home.html',context)
				except Delivery_Customer.DoesNotExist:
					customer = Delivery_Customer()
					customer.mobile = mob.mobile
					customer.address = ""
					customer.save()
					cust_id = customer.id
					return redirect('../Delivery/Invoice/Customer/'+str(cust_id)+'/Edit/',customer_id=cust_id)
			context={'form':form,"opened_inv":opened_inv,'all_invoices':all_invoices}
			return render(request,'Delivery/delivery_home.html',context)
		else:
			return render(request,'BASE/forbidden.html')

def Delivery_add_address(request,customer_id):
	if not request.user.is_authenticated():
		return render(request,'BASE/login.html')
	else:
		if perm(request,request.user,"is_delivery_taker") == True or perm(request,request.user,"is_delivery_admin") == True:
			this_customer = Delivery_Customer.objects.filter(pk = customer_id)[:1].get()
			mob_no = this_customer.mobile
			form = Delivery_Edit_CustomerForm(request.POST or None)
			if form.is_valid():
				new_address = form.save(commit = False)
				new_address.mobile = mob_no
				new_address.save()
				cust_id = new_address.id
				return redirect('../../' + str(cust_id))
			context = {'form':form}
			return render(request,'Delivery/delivery_customer_edit.html',context)
		else:
			return render(request,'BASE/forbidden.html')

def Delivery_customer_edit(request,customer_id):
	if not request.user.is_authenticated():
		return render(request,'BASE/login.html')
	else:
		if perm(request,request.user,"is_delivery_taker") == True or perm(request,request.user,"is_delivery_admin") == True:
			form = Delivery_Edit_CustomerForm(request.POST or None)
			if form.is_valid():
				customer = Delivery_Customer.objects.get(pk=customer_id)
				new_info = form.save(commit=False)
				customer.address = new_info.address
				customer.save()
				return redirect('../')
			context = {"form":form}
			return render(request,'Delivery/delivery_customer_edit.html',context)
		else:
			return render(request,'BASE/forbidden.html')

def Delivery_add_invoice(request,customer_id):
	if not request.user.is_authenticated():
		return render(request,'BASE/login.html')
	else:
		if perm(request,request.user,"is_delivery_taker") == True or perm(request,request.user,"is_delivery_admin") == True:
			customer = Delivery_Customer.objects.get(pk=customer_id)
			new_inv = Delivery_Invoice()
			new_inv.customer = customer
			new_inv.date = datetime.now()
			new_inv.is_shipped = False
			new_inv.is_closed = False
			new_inv.total_price = 0
			new_inv.save()
			return redirect('../../' + str(new_inv.id) +'/Categories/', inv_id = new_inv.id)
		else:
			return render(request,'BASE/forbidden.html')

def Delivery_categories(request,inv_id):
	if not request.user.is_authenticated():
		return render(request,'BASE/login.html')
	else:
		if perm(request,request.user,"is_delivery_taker") == True or perm(request,request.user,"is_delivery_admin") == True:
			all_cat = Item_Category.objects.all()
			inv_items = Delivery_Invoice_Items.objects.filter(invoice_id=inv_id)
			this_inv = Delivery_Invoice.objects.get(id=inv_id)
			opened_inv = Delivery_Invoice.objects.filter(is_closed =False)
			context={'all_cat':all_cat,"inv_items":inv_items,"inv_id":inv_id,"this_inv":this_inv,"opened_inv":opened_inv}
			return render(request,'Delivery/cash_categories.html',context)
		else:
			return render(request,'BASE/forbidden.html')

def Delivery_items(request,inv_id,cat_id):
	if not request.user.is_authenticated():
		return render(request,'BASE/login.html')
	else:
		if perm(request,request.user,"is_delivery_taker") == True or perm(request,request.user,"is_delivery_admin") == True:
			all_items = Item.objects.filter(category = cat_id)
			inv_items = Delivery_Invoice_Items.objects.filter(invoice_id=inv_id)
			this_inv = Delivery_Invoice.objects.get(id=inv_id)
			opened_inv = Delivery_Invoice.objects.filter(is_closed =False)
			context={'all_items':all_items,"inv_items":inv_items,"inv_id":inv_id,"this_inv":this_inv,"opened_inv":opened_inv}
			return render(request,'Delivery/cash_items.html',context)
		else:
			return render(request,'BASE/forbidden.html')

def Delivery_add_item(request,inv_id,item_id):
	if not request.user.is_authenticated():
		return render(request,'BASE/login.html')
	else:
		if perm(request,request.user,"is_delivery_taker") == True or perm(request,request.user,"is_delivery_admin") == True:
			selected_inv = get_object_or_404(Delivery_Invoice,pk=inv_id)
			selected_item = get_object_or_404(Item,pk = item_id)
			add_item = Delivery_Invoice_Items()
			add_item.invoice_id = selected_inv
			add_item.item = selected_item
			add_item.quantity = 1
			if selected_item.stock_managed == True:
				warehouse = get_warehouse(request,request.user)
				if warehouse_has_stock(request,warehouse,add_item.item,add_item.quantity) == False:
					error_message = "لا يوجد مخزون كافي من المنتج " + add_item.item.name
					context = {"error_message":error_message}
					return render(request,'BASE/error.html',context)
				else:			
					pass
			add_item.unit_price = selected_item.price
			add_item.total_price = selected_item.price * 1
			add_item.save()
			all_cat = Item_Category.objects.all()
			inv_items = Delivery_Invoice_Items.objects.filter(invoice_id=inv_id)
			return redirect('../../Categories/')
		else:
			return render(request,'BASE/forbidden.html')

def Delivery_increase_quantity(request,inv_id,inv_item_id):
	if not request.user.is_authenticated():
		return render(request,'BASE/login.html')
	else:
		if perm(request,request.user,"is_delivery_taker") == True or perm(request,request.user,"is_delivery_admin") == True:
			selected_item = Delivery_Invoice_Items.objects.get(pk=inv_item_id)
			selected_item.quantity += 1
			if selected_item.item.stock_managed == True:
				warehouse = get_warehouse(request,request.user)
				if warehouse_has_stock(request,warehouse,selected_item.item,selected_item.quantity) == False:
					error_message = "لا يوجد مخزون كافي من المنتج " + selected_item.item.name
					context = {"error_message":error_message}
					return render(request,'BASE/error.html',context)
				else:
					pass
			selected_item.total_price += selected_item.unit_price
			selected_item.save()
			return redirect('../../Categories/')
		else:
			return render(request,'BASE/forbidden.html')



def Delivery_decrease_quantity(request,inv_id,inv_item_id):
	if not request.user.is_authenticated():
		return render(request,'BASE/login.html')
	else:
		if perm(request,request.user,"is_delivery_taker") == True or perm(request,request.user,"is_delivery_admin") == True:
			selected_item = Delivery_Invoice_Items.objects.get(pk=inv_item_id)
			selected_item.quantity -= 1
			selected_item.total_price -= selected_item.unit_price
			selected_item.save()
			return redirect('../../Categories/')
		else:
			return render(request,'BASE/forbidden.html')
		

def Delivery_delete_invoice_item(request,inv_id,inv_item_id):
	if not request.user.is_authenticated():
		return render(request,'BASE/login.html')
	else:
		if perm(request,request.user,"is_delivery_taker") == True or perm(request,request.user,"is_delivery_admin") == True:
			this_inv = Delivery_Invoice.objects.get(pk = inv_id)
			if this_inv.is_closed == False:
				selected_item = Delivery_Invoice_Items.objects.get(pk=inv_item_id)
				selected_item.delete()
				return redirect('../../Categories/')
			else:
				if perm(request,request.user,"is_delivery_admin") == True:
					selected_item = Delivery_Invoice_Items.objects.get(pk=inv_item_id)
					selected_item.delete()
					return redirect('../../Categories/')
				else:
					return render(request,'BASE/forbidden.html')
		else:
			return render(request,'BASE/forbidden.html')


def Delivery_delete_invoice(request,inv_id):
	if not request.user.is_authenticated():
		return render(request,'BASE/login.html')
	else:
		if perm(request,request.user,"is_delivery_admin") == True:
			selected_invoice = Delivery_Invoice.objects.get(pk=inv_id)
			selected_invoice.delete()
			return redirect('../../../../')
		else:
			return render(request,'BASE/forbidden.html')

def Delivery_close_invoice(request,inv_id):
	if not request.user.is_authenticated():
		return render(request,'BASE/login.html')
	else:
		if perm(request,request.user,"is_delivery_taker") == True or perm(request,request.user,"is_delivery_admin") == True:
			selected_inv = Delivery_Invoice.objects.get(pk=inv_id)
			selected_inv.is_closed = True
			selected_inv.user = request.user
			selected_inv.save()
			emp = User_Admin.objects.get(user = request.user)
			inv_total = 0.0
			inv_items = Delivery_Invoice_Items.objects.filter(invoice_id = inv_id)
			for x in inv_items:
				inv_total += x.total_price
			selected_inv.total_price = inv_total
			selected_inv.save()
			return redirect('../Categories/')
		else:
			return render(request,'BASE/forbidden.html')

def Delivery_shipping(request,inv_id):
	if not request.user.is_authenticated():
		return render(request,'BASE/login.html')
	else:
		if perm(request,request.user,"is_delivery_admin") == True:
			this_entry = Delivery_Invoice.objects.get(pk = inv_id)
			delivery_pilots = User_Admin.objects.filter(is_delivery_pilot = True)
			form = Shipping_Form(request.POST or None, instance=this_entry)
			if form.is_valid():	
				shipped_with = request.POST.get("shipped_with")
				pilot = User_Admin.objects.get(pk = shipped_with)
				this_inv = Delivery_Invoice.objects.get(pk = inv_id)
				this_inv.is_shipped = True
				this_inv.shipped_with = pilot
				this_inv.shipping_date = datetime.now()
				pilot.credit -= this_inv.total_price
				this_inv.save()
				pilot.save()
				return redirect('/ERP/')
			else:
				context = {'form':form,'this_entry':this_entry,"delivery_pilots":delivery_pilots}
				return render(request,'Delivery/delivery_shipping.html',context)
				

def Delivery_print_invoice(request,inv_id):
	if not request.user.is_authenticated():
		return render(request,'BASE/login.html')
	else:
		if perm(request,request.user,"is_delivery_taker") == True or perm(request,request.user,"is_delivery_admin") == True:
			this_inv = Delivery_Invoice.objects.get(id=inv_id)
			if this_inv.is_closed == True:
				this_customer = Delivery_Customer.objects.get(pk = this_inv.customer.id)
				inv_items = Delivery_Invoice_Items.objects.filter(invoice_id=inv_id)
				inv_total = 0
				for x in inv_items:
					inv_total += x.total_price
				context = {"this_inv":this_inv,"inv_items":inv_items,"inv_total":inv_total,"this_customer":this_customer}
				return render(request, 'BASE/invoice.html',context)
			else:
				if perm(request,request.user,"is_delivery_admin") == True:
					this_customer = Delivery_Customer.objects.get(pk = this_inv.customer.id)
					inv_items = Delivery_Invoice_Items.objects.filter(invoice_id=inv_id)
					inv_total = 0
					for x in inv_items:
						inv_total += x.total_price
					context = {"this_inv":this_inv,"inv_items":inv_items,"inv_total":inv_total,"this_customer":this_customer}
					return render(request, 'BASE/invoice.html',context)	
				else:
					return render(request,'BASE/forbidden.html')
		else:
			return render(request,'BASE/forbidden.html')