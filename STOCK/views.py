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
def stock_home(request):	
	if not request.user.is_authenticated():
		return render(request,'BASE/login.html')
	else:
		return render(request,'STOCK/stock_home.html')

def stock_transfer(request):
	if not request.user.is_authenticated():
		return render(request,'BASE/login.html')
	else:
		all_stock = Warehouse_Stock.objects.all()
		pending_transfers = Warehouse_Transfer_Transaction.objects.filter(is_recieved=False)
		error_message = ""
		form = Warehouse_Transfer_Transaction_Form(request.POST or None)
		if form.is_valid():
			trans = form.save(commit=False)
			try:
				source_warehouse = Warehouse_Stock.objects.get(item = trans.item , warehouse = trans.from_warehouse)
				if source_warehouse.quantity >= trans.quantity:
					source_warehouse.quantity -= trans.quantity
					source_warehouse.save()
					trans.is_recieved = False
					trans.user = request.user
					trans.save()
					error_message = "تم التحويل بنجاح"
				else:
					error_message = "لا يوجد رصيد كافي"
			except Warehouse_Stock.DoesNotExist:
				error_message = "لا يوجد رصيد كافي"
			
			context = {'form':form,'error_message':error_message,'all_stock':all_stock,'pending_transfers':pending_transfers}
			return render(request,"STOCK/stock_transfer.html",context)
		context = {'form':form,'error_message':error_message,'all_stock':all_stock,'pending_transfers':pending_transfers}
		return render(request,"STOCK/stock_transfer.html",context)

def stock_recieve_transfer(request,trans_id):
	if not request.user.is_authenticated():
		return render(request,'BASE/login.html')
	else:
		all_stock = Warehouse_Stock.objects.all()		
		trans = Warehouse_Transfer_Transaction.objects.get(id = trans_id)
		form = Warehouse_Transfer_Transaction_Form(request.POST or None)
		if trans.is_recieved == True:
			error_message = "تم استلام التحويل بالفعل"
		else:
			error_message = ""
			try:
				target_warehouse = Warehouse_Stock.objects.get(item = trans.item , warehouse = trans.to_warehouse)
				target_warehouse.quantity += trans.quantity
			except Warehouse_Stock.DoesNotExist:
				target_warehouse = Warehouse_Stock()
				target_warehouse.warehouse = trans.to_warehouse
				target_warehouse.item = trans.item
				target_warehouse.quantity = trans.quantity
			target_warehouse.save()
			trans.is_recieved = True
			trans.recieved_by = request.user
			trans.save()
			error_message = "تم الاستلام بنجاح"
			context = {'form':form,'error_message':error_message,'all_stock':all_stock}
			return render(request,"STOCK/stock_transfer.html",context)
	context = {'form':form,'error_message':error_message,'all_stock':all_stock}
	return render(request,"STOCK/stock_transfer.html",context)

def stock_warehouse(request):
	if not request.user.is_authenticated():
		return render(request,'BASE/login.html')
	else:
		all_warehouses = Warehouse.objects.all()
		form = Warehouse_Form(request.POST or None)
		if form.is_valid():
			warehouse = form.save(commit = False)
			warehouse.save()
			stock = Warehouse
			context = {"all_warehouses":all_warehouses,"form":form}
			return render(request,'STOCK/setting_warehouse.html',context)
		context = {"all_warehouses":all_warehouses,"form":form}
		return render(request,'STOCK/setting_warehouse.html',context)

def stock_add(request):
	if not request.user.is_authenticated():
		return render(request,'BASE/login.html')
	else:
		all_stock = Warehouse_Stock.objects.all()
		form = Stock_Add_Form(request.POST or None)
		if form.is_valid():
			new_stock = form.save(commit=False)
			try:
				old_stock = Warehouse_Stock.objects.get(item = new_stock.item , warehouse = new_stock.warehouse)
				old_stock.quantity += new_stock.quantity
				old_stock.save()
			except Warehouse_Stock.DoesNotExist:
				new_stock.save()

			context = {"form":form,"all_stock":all_stock}
			return render(request,'STOCK/stock_add.html',context)
		context = {"form":form,"all_stock":all_stock}
		return render(request,'STOCK/stock_add.html',context)

def stock_search(request):
	if not request.user.is_authenticated():
		return render(request,'BASE/login.html')
	else:
		error_message = ""
		form = Stock_Search_Form(request.POST or None)
		if form.is_valid():
			selected_item = form.save(commit = False)
			search_result = Warehouse_Stock.objects.filter(item = selected_item.item)
			if search_result.count() == 0:
				error_message = "لا يوجد أي مخزون من هذا المنتج"
			context = {'form':form , 'search_result':search_result,"error_message":error_message}
			return render(request,'STOCK/stock_search.html',context)
		context = {"form":form}
		return render(request,'STOCK/stock_search.html',context)
