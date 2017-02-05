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
def home(request):
	if not request.user.is_authenticated():
		return render(request,'BASE/login.html')
	else:
		return render(request,"Manufacture/home.html")

def new_order(request):
	if not request.user.is_authenticated():
		return render(request,'BASE/login.html')
	else:
		title = "بدأ دورة إنتاج"
		all_entries = Production_Order.objects.all()
		form = Production_Order_Form(request.POST or None)
		if form.is_valid():
			entry = form.save(commit = False)
			entry.save()
			return redirect('../Order/'+ str(entry.id) +'/Raw_Materials/')
		context = {'form':form,'title':title,'all_entries':all_entries}
		return render(request,'Manufacture/new_order.html',context)

def raw_materials(request,order_id):
	if not request.user.is_authenticated():
		return render(request,'BASE/login.html')
	else:
		title = "إضافة مواد خام"
		order_items = Production_Raw_Material.objects.filter(order = order_id)
		all_items = Item.objects.filter(raw_material= True)
		order = Production_Order.objects.get(pk = order_id)
		form = Raw_Material_Form(request.POST or None)
		if form.is_valid():
			entry = form.save(commit = False)
			item = Item.objects.get(pk = request.POST.get('item'))
			entry.order = order
			entry.item = item
			entry.save()
			context = {'form':form , 'title':title , 'order_items':order_items,'all_items':all_items,'order':order}
			return render(request,'Manufacture/raw_materials.html',context)
		context = {'form':form , 'title':title , 'order_items':order_items,'all_items':all_items,'order':order}
		return render(request,'Manufacture/raw_materials.html',context)
	

def end_products(request,order_id):
	if not request.user.is_authenticated():
		return render(request,'BASE/login.html')
	else:
		title = "إضافة  منتج مصنع"
		order_items = Production_Finished_Product.objects.filter(order = order_id)
		all_items = Item.objects.filter(produced_item = True)
		order = Production_Order.objects.get(pk = order_id)
		form = End_Products_Form(request.POST or None)
		if form.is_valid():
			entry = form.save(commit = False)
			item = Item.objects.get(pk = request.POST.get('item'))
			entry.order = order
			entry.item = item
			entry.save()
			context = {'form':form , 'title':title , 'order_items':order_items,'all_items':all_items,'order':order}
			return render(request,'Manufacture/end_products.html',context)
		context = {'form':form , 'title':title , 'order_items':order_items,'all_items':all_items,'order':order}
		return render(request,'Manufacture/end_products.html',context)
def deduct_from_stock(request,order_id):
	if not request.user.is_authenticated():
		return render(request,'BASE/login.html')
	else:
		this_entry = Production_Order.objects.get(pk = order_id)
		this_warehouse = this_entry.from_stock
		for x in Production_Raw_Material.objects.filter(order = order_id):
			warehouse_stock = Warehouse_Stock.objects.get(warehouse = this_warehouse, item = x.item)
			warehouse_stock.quantity -= x.amount
			warehouse_stock.save()
		
def start_production(request,order_id):
	if not request.user.is_authenticated():
		return render(request,'BASE/login.html')
	else:
		this_entry = Production_Order.objects.get(pk = order_id)
		this_warehouse = this_entry.from_stock
		if this_entry.is_started == True:
			error_message = "تم بدأ هذه الدورة بالفعل"
			context = {'error_message':error_message}
			return render(request,'Manufacture/raw_materials.html',context)
		else:
			for x in Production_Raw_Material.objects.filter(order = order_id):
				try:
					warehouse_stock = Warehouse_Stock.objects.get(warehouse = this_warehouse, item=x.item)
					if warehouse_stock.quantity < x.amount:
						error_message = "لا يوجد مخزون كافي من الصنف " + x.item.name + " في المخزن " + warehouse_stock.warehouse.name
						context = {'error_message':error_message}
						return render(request,'Manufacture/raw_materials.html',context)
					else:
						warehouse_stock.quantity -= x.amount
						continue
				except Warehouse_Stock.DoesNotExist:
					error_message = "لا يوجد مخزون من هذا الصنف في هذا المخزن"  + x.item.name + " في المخزن " + this_warehouse.name
					context = {'error_message':error_message}
					return render(request,'Manufacture/raw_materials.html',context)
			deduct_from_stock(request,order_id)
			this_entry.start_date = datetime.now()
			this_entry.is_started = True
			this_entry.save()
			return redirect('../Raw_Materials/')

def finish_production(request,order_id):
	if not request.user.is_authenticated():
		return render(request,'BASE/login.html')
	else:
		this_entry = Production_Order.objects.get(pk = order_id)
		if this_entry.is_started == False:
			error_message = "لم يتم بدء هذه الدورة بعد"
			context = {'error_message':error_message}
			return render(request,'Manufacture/raw_materials.html',context)
		else:
			this_warehouse = this_entry.to_stock
			for x in this_entry.get_end():
				try:
					warehouse_stock = Warehouse_Stock.objects.get(warehouse = this_warehouse, item=x.item)
					warehouse_stock.quantity += x.amount
				except Warehouse_Stock.DoesNotExist:
					warehouse_stock = Warehouse_Stock()
					warehouse_stock.warehouse = this_warehouse
					warehouse_stock.item = x.item
					warehouse_stock.quantity = x.amount
				warehouse_stock.save()
			this_entry.finish_date = datetime.now()
			this_entry.is_finished = True
			this_entry.save()
			return redirect('../End_Products/')

def delete_order(request,order_id):
	if not request.user.is_authenticated():
		return render(request,'BASE/login.html')
	else:
		this_entry = Production_Order.objects.get(pk = order_id)
		this_entry.delete()
		return redirect(reverse('MANUFACTURE:new_order'))

def detailed_report(request,order_id):
	if not request.user.is_authenticated():
		return render(request,'BASE/login.html')
	else:
		this_entry = Production_Order.objects.get(pk = order_id)
		all_raw = this_entry.get_raw()
		all_end = this_entry.get_end()
		context = {'this_entry':this_entry, 'all_raw':all_raw, 'all_end':all_end}
		return render(request,'Manufacture/detailed_report.html',context)

def production_report(request):
	if not request.user.is_authenticated():
		return render(request,'BASE/login.html')
	else:
		all_entries = Production_Order.objects.all()
		context = {'all_entries':all_entries}
		return render(request,'Manufacture/report.html',context)

def delete_raw_materials(request,order_id,raw_id):
	if not request.user.is_authenticated():
		return render(request,'BASE/login.html')
	else:
		this_entry = Production_Raw_Material.objects.get(pk = raw_id)
		order_id = this_entry.order.id
		if this_entry.order.is_started == True:
			error_message = "لا يمك تعديل امر التصنيع بعد البدء"
			context = {"error_message":error_message}
			return render(request,'Manufacture/raw_materials.html',context)
		else:
			this_entry.delete()
			return redirect(reverse("MANUFACTURE:raw_materials",args=(order_id,)))

def delete_end_products(request,order_id,end_id):
	if not request.user.is_authenticated():
		return render(request,'BASE/login.html')
	else:
		this_entry = Production_Finished_Product.objects.get(pk = end_id)
		order_id = this_entry.order.id
		if this_entry.order.is_finished == True:
			error_message = "لا يمك تعديل امر التصنيع بعد تخزين المنتج"
			context = {"error_message":error_message}
			return render(request,'Manufacture/raw_materials.html',context)
		else:
			this_entry.delete()
			return redirect(reverse("MANUFACTURE:end_products",args=(order_id,)))
