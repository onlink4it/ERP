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

def POS_home(request):
	if not request.user.is_authenticated():
		return render(request, 'BASE/login.html')
	else:
		unpaid_invoices = POS_Invoice.objects.filter(is_closed=False)
		all_customers = POS_Customer.objects.all()
		form = POS_Add_Invoice_Form(request.POST or None)
		if form.is_valid():
			x = form.save(commit=False)
			x.date = datetime.now()
			x.save()
			return redirect('../POS/Invoice/' + str(x.id) + '/Categories/' , inv_id = x.id)
		context = {"form":form,"all_customers":all_customers,"unpaid_invoices":unpaid_invoices}
		return render(request,'POS/home.html',context)
	

def POS_categories(request,inv_id):
	if not request.user.is_authenticated():
		return render(request,'BASE/login.html')
	else:
		all_cat = Item_Category.objects.all()
		inv_items = POS_Invoice_Items.objects.filter(invoice=inv_id)
		this_inv = POS_Invoice.objects.get(id=inv_id)
		opened_inv = POS_Invoice.objects.filter(is_closed =False)
		context={'all_cat':all_cat,"inv_items":inv_items,"inv_id":inv_id,"this_inv":this_inv,"opened_inv":opened_inv}
		return render(request,'POS/categories.html',context)


def POS_items(request,inv_id,cat_id):
	if not request.user.is_authenticated():
		return render(request,'BASE/login.html')
	else:
		all_items = Item.objects.filter(category = cat_id)
		inv_items = POS_Invoice_Items.objects.filter(invoice=inv_id)
		this_inv = POS_Invoice.objects.get(id=inv_id)
		opened_inv = POS_Invoice.objects.filter(is_closed =False)
		context={'all_items':all_items,"inv_items":inv_items,"inv_id":inv_id,"this_inv":this_inv,"opened_inv":opened_inv}
		return render(request,'POS/items.html',context)

def POS_add_item(request,inv_id,item_id):
	if not request.user.is_authenticated():
		return render(request,'BASE/login.html')
	else:
		selected_inv = get_object_or_404(POS_Invoice,pk=inv_id)
		selected_item = get_object_or_404(Item,pk = item_id)
		add_item = POS_Invoice_Items()
		add_item.invoice = selected_inv
		add_item.item = selected_item
		add_item.quantity = 1
		add_item.unit_price = selected_item.price
		add_item.total_price = selected_item.price * 1
		add_item.save()
		all_cat = Item_Category.objects.all()
		inv_items = POS_Invoice_Items.objects.filter(invoice=inv_id)
		return redirect('../../Categories/')

def POS_increase_quantity(request,inv_id,inv_item_id):
	if not request.user.is_authenticated():
		return render(request,'BASE/login.html')
	else:
		selected_item = POS_Invoice_Items.objects.get(pk=inv_item_id)
		selected_item.quantity += 1
		selected_item.total_price += selected_item.unit_price
		selected_item.save()
		return redirect('../../Categories/')



def POS_decrease_quantity(request,inv_id,inv_item_id):
	if not request.user.is_authenticated():
		return render(request,'BASE/login.html')
	else:
		selected_item = POS_Invoice_Items.objects.get(pk=inv_item_id)
		selected_item.quantity -= 1
		selected_item.total_price -= selected_item.unit_price
		selected_item.save()
		return redirect('../../Categories/')

def POS_delete_invoice_item(request,inv_id,inv_item_id):
	if not request.user.is_authenticated():
		return render(request,'BASE/login.html')
	else:
		selected_item = POS_Invoice_Items.objects.get(pk=inv_item_id)
		selected_item.delete()
		return redirect('../../Categories/')



def POS_close_invoice(request,inv_id):
	if not request.user.is_authenticated():
		return render(request,'BASE/login.html')
	else:
		selected_inv = POS_Invoice.objects.get(pk=inv_id)
		selected_inv.is_closed = True
		selected_inv.save()
		selected_customer = POS_Customer.objects.get(id = selected_inv.customer.id)
		inv_total = 0.0
		inv_items = POS_Invoice_Items.objects.filter(invoice = inv_id)
		for x in inv_items:
			inv_total += x.total_price
		selected_customer.credit -= inv_total
		selected_customer.save()
		return redirect('../Categories/')

def POS_pay_invoice(request,inv_id):
	if not request.user.is_authenticated():
		return render(request,'BASE/login.html')
	else:
		selected_inv = POS_Invoice.objects.get(pk = inv_id)
		selected_inv_items = POS_Invoice_Items.objects.filter(invoice = inv_id)
		inv_total = 0
		for x in selected_inv_items:
			inv_total += x.total_price	
		selected_customer = POS_Customer.objects.get(id = selected_inv.customer.id)
		selected_customer.credit += inv_total
		curr_user = User_Admin.objects.get(user = request.user)
		curr_user.credit -= inv_total
		trans = POS_Transactions()
		trans.date = datetime.now()
		trans.customer = selected_customer
		trans.amount = inv_total
		trans.paid_to = request.user
		trans.save()
		selected_customer.save()
		curr_user.save()
		return redirect('../../../')

def POS_print_invoice(request,inv_id):
	if not request.user.is_authenticated():
		return render(request,'BASE/login.html')
	else:
		this_inv = POS_Invoice.objects.get(id=inv_id)
		inv_items = POS_Invoice_Items.objects.filter(invoice=inv_id)
		inv_total = 0
		for x in inv_items:
			inv_total += x.total_price
		context = {"this_inv":this_inv,"inv_items":inv_items,"inv_total":inv_total}
		return render(request, 'BASE/invoice.html',context)

def POS_add_customer(request):
	if not request.user.is_authenticated():
		return render(request,'BASE/login.html')
	else:
		all_customers = POS_Customer.objects.all()
		form = POS_CustomerForm(request.POST or None)
		if form.is_valid():
			customer = form.save(commit=False)
			customer.save()
			context = {"form":form,"all_customers":all_customers}
			return render(request,'POS/add_customer.html',context)
		context = {"form":form,"all_customers":all_customers}
		return render(request,'POS/add_customer.html',context)