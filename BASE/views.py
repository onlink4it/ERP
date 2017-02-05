# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate, login, logout
from django.template import loader
from datetime import date,datetime
from django.urls import reverse
from django import forms
from .models import *
from .forms import *
from django.shortcuts import render,get_object_or_404,redirect

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
	if permission == "is_superuser":
		if employee.is_superuser == True:
			return True
		else:
			return False



# Create your views here.
def index(request):
	if not request.user.is_authenticated():
		return render(request, 'BASE/login.html')
	else:
		authorized_array = [perm(request,request.user,'is_pos_employee'),perm(request,request.user,'is_pos_admin'),perm(request,request.user,'is_delivery_taker'),perm(request,request.user,'is_delivery_admin'),perm(request,request.user,'is_product_admin'),perm(request,request.user,'is_invoice_admin'),perm(request,request.user,'is_purchases_admin'),perm(request,request.user,'is_stock_admin'),perm(request,request.user,'is_user_admin'),perm(request,request.user,'is_accounts_admin'),]
		context = {'authorized_array':authorized_array}
		return render(request,"BASE/index.html",context)

def system_setting(request):
	if not request.user.is_authenticated():
		return render(request, 'BASE/login.html')
	else:
		authorized_array = [perm(request,request.user,'is_product_admin'),perm(request,request.user,'is_invoice_admin'),perm(request,request.user,'is_user_admin'),]
		authorized = False
		for x in authorized_array:
			if  x == True:
				authorized = True
		if authorized == True:
			context = {'authorized_array':authorized_array}
			return render(request, "BASE/system_setting.html",context)
		else:
			return render(request,"BASE/forbidden.html")

def user_accounts(request):
	if not request.user.is_authenticated():
		return render(request, 'BASE/login.html')
	else:
		if perm(request,request.user,"is_user_admin") == True:
			all_emp = User.objects.all()
			form = UserForm(request.POST or None)
			if form.is_valid():
				user = form.save(commit=False)
				username = form.cleaned_data['username']
				password = form.cleaned_data['password']
				user.set_password(password)
				user_id = user.id
				user.save()
			context = {"form":form, "all_emp":all_emp,}
			return render(request,"BASE/user_accounts.html",context)
		else:
			return render(request,"BASE/forbidden.html")

def user_perm(request,user_id):
	if not request.user.is_authenticated():
		return render(request, 'BASE/login.html')
	else:
		if perm(request,request.user,"is_user_admin") == True:
			all_emp = User_Admin.objects.all()
			emp_user = User.objects.get(pk = user_id)
			form = User_Admin_Form(request.POST or None)
			if form.is_valid():
				new_emp = form.save(commit = False)
				try:
					emp_exist = User_Admin.objects.get(user = emp_user)
					emp_exist.is_pos_employee =new_emp.is_pos_employee
					emp_exist.is_pos_admin =new_emp.is_pos_admin
					emp_exist.is_delivery_taker =new_emp.is_delivery_taker
					emp_exist.is_delivery_admin =new_emp.is_delivery_admin
					emp_exist.is_product_admin =new_emp.is_product_admin
					emp_exist.is_invoice_admin =new_emp.is_invoice_admin
					emp_exist.is_purchases_admin =new_emp.is_purchases_admin
					emp_exist.is_stock_admin =new_emp.is_stock_admin
					emp_exist.is_user_admin =new_emp.is_user_admin
					emp_exist.is_accounts_admin =new_emp.is_accounts_admin
					emp_exist.save()
					error_message = ""
					context = {"form":form,"error_message":error_message,"all_emp":all_emp}
					return render(request,"BASE/user_perm.html",context)
				except User_Admin.DoesNotExist:
					new_emp.user = emp_user
					new_emp.save()
			context = {"form":form,"all_emp":all_emp}
			return render(request,"BASE/user_perm.html",context)
		else:
			return render(request,"BASE/forbidden.html")

		
def add_category(request):
	if not request.user.is_authenticated():
		return render(request, 'BASE/login.html')
	else:
		if perm(request,request.user,"is_product_admin") == True:
			all_categories = Item_Category.objects.all()
			form = Item_Category_Form(request.POST or None)
			if form.is_valid():
				cat = form.save(commit=False)
				cat.save()
				context = {"form":form,"all_categories":all_categories}
				return render(request,'BASE/add_category.html',context)
			context = {"form":form,"all_categories":all_categories}
			return render(request,'BASE/add_category.html',context)
		else:
			return render(request,"BASE/forbidden.html")

def edit_category(request):
	if not request.user.is_authenticated():
		return render(request, 'BASE/login.html')
	else:
		if perm(request,request.user,"is_product_admin") == True:
			all_categories = Item_Category.objects.all()
			form = Item_Category_Form(request.POST or None)
			if form.is_valid():
				cat = form.save(commit=False)
				cat.save()
				context = {"form":form,"all_categories":all_categories}
				return render(request,'BASE/add_category.html',context)
			context = {"form":form,"all_categories":all_categories}
			return render(request,'BASE/add_category.html',context)
		else:
			return render(request,"BASE/forbidden.html")

def add_category(request):
	if not request.user.is_authenticated():
		return render(request, 'BASE/login.html')
	else:
		if perm(request,request.user,"is_product_admin") == True:
			all_categories = Item_Category.objects.all()
			form = Item_Category_Form(request.POST or None)
			if form.is_valid():
				cat = form.save(commit=False)
				cat.save()
				context = {"form":form,"all_categories":all_categories}
				return render(request,'BASE/add_category.html',context)
			context = {"form":form,"all_categories":all_categories}
			return render(request,'BASE/add_category.html',context)
		else:
			return render(request,"BASE/forbidden.html")

def add_product(request):
	if not request.user.is_authenticated():
		return render(request, 'BASE/login.html')
	else:
		if perm(request,request.user,"is_product_admin") == True:
			all_categories = Item.objects.all()
			form = Item_Form(request.POST or None)
			if form.is_valid():
				cat = form.save(commit=False)
				cat.save()
				context = {"form":form,"all_categories":all_categories}
				return render(request,'BASE/add_product.html',context)
			context = {"form":form,"all_categories":all_categories}
			return render(request,'BASE/add_product.html',context)
		else:
			return render(request,"BASE/forbidden.html")

def edit_product(request,product_id):
	if not request.user.is_authenticated():
		return render(request, 'BASE/login.html')
	else:
		if perm(request,request.user,"is_product_admin") == True:				
			this_entry = Item.objects.get(pk = product_id)
			form = Item_Form(request.POST or None , instance = this_entry)	
			if form.is_valid():		
				form.save()
				return redirect('../../Add/')
			else:
				context = {'form':form}
				return render(request,'BASE/add_product.html/',context)
		else:
			return render(request,"BASE/forbidden.html")



def add_expense_category(request):
	if not request.user.is_authenticated():
		return render(request, 'BASE/login.html')
	else:
		if perm(request,request.user,"is_accounts_admin") == True:
			all_categories = Expense_Category.objects.all()
			form = Expense_Category_Form(request.POST or None)
			if form.is_valid():
				cat = form.save(commit=False)
				cat.save()
				context = {"form":form,"all_categories":all_categories}
				return render(request,'BASE/accounts/add_expense.html',context)
			context = {"form":form,"all_categories":all_categories}
			return render(request,'BASE/accounts/add_expense_category.html',context)
		else:
			return render(request,"BASE/forbidden.html")

def delete_expense_category(request,cat_id):
	if not request.user.is_authenticated():
		return render(request, 'BASE/login.html')
	else:
		if perm(request,request.user,"is_accounts_admin") == True:
			this_entry = Expense_Category.objects.get(pk = cat_id)
			this_entry.delete()
			return redirect('../../')
		else:
			return render(request,"BASE/forbidden.html")

def add_expense(request):
	if not request.user.is_authenticated():
		return render(request, 'BASE/login.html')
	else:
		if perm(request,request.user,"is_accounts_admin") == True:
			all_entries = Expense_Transaction.objects.all()
			title = ""
			form = Expense_Transaction_Form(request.POST or None)
			if form.is_valid():
				trans = form.save(commit=False)
				trans.date = datetime.now()
				trans.save()
				treasury_trans = Treasury()
				treasury_trans.date = datetime.now()
				treasury_trans.amount = -trans.amount
				treasury_trans.comment = trans.category.name + " " + trans.comment
				trans.save()
				treasury_trans.save()
				context = {"form":form,"all_entries":all_entries,"title":title}
				return render(request,'BASE/accounts/add_expense.html',context)
			context = {"form":form,"all_entries":all_entries,"title":title}
			return render(request,'BASE/accounts/add_expense.html',context)
		else:
			return render(request,"BASE/forbidden.html")

def edit_expense(request,expense_id):
	if not request.user.is_authenticated():
		return render(request, 'BASE/login.html')
	else:
		if perm(request,request.user,"is_accounts_admin") == True:
			title = ""
			all_entries = Expense_Transaction.objects.all()
			this_entry = Expense_Transaction.objects.get(pk = expense_id)	
			form = Expense_Transaction_Form(request.POST or None,instance = this_entry)
			if form.is_valid():
				form.save()
				return redirect("../../")
			else:
				context = {"form":form,"all_entries":all_entries,"title":title}
				return render(request,"BASE/accounts/add_expense.html",context)
		else:
			return render(request,"BASE/forbidden.html")


def delete_expense(request,expense_id):
	if not request.user.is_authenticated():
		return render(request, 'BASE/login.html')
	else:
		if perm(request,request.user,"is_accounts_admin") == True:
			this_entry = Expense_Transaction.objects.get(pk = expense_id)
			this_entry.delete()
			return redirect('../../')
		else:
			return render(request,"BASE/forbidden.html")

def accounts_home(request):
	if not request.user.is_authenticated():
		return render(request, 'BASE/login.html')
	else:
		if perm(request,request.user,"is_accounts_admin") == True:
			return render(request,'BASE/accounts/accounts_home.html')
		else:
			return render(request,"BASE/forbidden.html")

def treasury(request):
	if not request.user.is_authenticated():
		return render(request, 'BASE/login.html')
	else:
		if perm(request,request.user,"is_accounts_admin") == True:
			treasury_trans = Treasury.objects.all()
			balance = 0
			for x in treasury_trans:
				balance += x.amount
			context = {'treasury_trans':treasury_trans,'balance':balance}
			return render(request,'BASE/accounts/treasury.html',context)
		else:
			return render(request,"BASE/forbidden.html")






















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

def inventory_home(request):
	if not request.user.is_authenticated():
		return render(request,'BASE/login.html')
	else:
		all_entries = Warehouse.objects.all()
		context = {'all_entries':all_entries}
		return render(request,'STOCK/inventory_home.html',context)

def inventory_print(request,warehouse_id):
	if not request.user.is_authenticated():
		return render(request,'BASE/login.html')
	else:
		this_entry = Warehouse.objects.get(pk = warehouse_id)
		all_entries = Warehouse_Stock.objects.filter(warehouse__id = warehouse_id)
		date = datetime.now()
		context = {'all_entries':all_entries,'this_entry':this_entry,'date':date}
		return render(request,'STOCK/inventory_print.html',context)




















def create_branch(request):
	if not request.user.is_authenticated():
		return render(request,'BASE/login.html')
	else:
		all_entries = Branch_Stock.objects.all()
		form = Branch_Form(request.POST or None)
		if form.is_valid():
			new_branch = form.save(commit = False)
			new_warehouse = Warehouse()
			new_warehouse.name = request.POST.get('name')
			new_warehouse.address = request.POST.get('address')
			new_branch.save()
			new_warehouse.save()
			new_link = Branch_Stock()
			new_link.branch = new_branch
			new_link.warehouse = new_warehouse
			new_link.save()
			return redirect(reverse('BASE:index'))
		context = {'form':form,'all_entries':all_entries}
		return render(request,'Branches/create.html',context)

def delete_branch(request,branch_id):
	if not request.user.is_authenticated():
		return render(request,'BASE/login.html')
	else:
		pass

def choose_branch(request):
	if not request.user.is_authenticated():
		return render(request,'BASE/login.html')
	else:
		form = Choose_Branch_Form(request.POST or None)
		if form.is_valid():
			try:
				branch_users = Branch_Users.objects.get(user = request.user)
			except Branch_Users.DoesNotExist:
				branch_users = Branch_Users()

			branch_id = request.POST.get('branch')
			branch = Branch.objects.get(pk = branch_id) 
			branch_users.branch = branch
			branch_users.user = request.user
			branch_users.warehouse = branch.get_warehouse()
			branch_users.save()
			return redirect(reverse("BASE:index"))
		context = {"form":form}
		return render(request,'Branches/choose_branch.html',context)
		











#####################################################################################################
#####################################################################################################
#####################################################################################################
#####################################################################################################
#####################################################################################################
########################################            AUTH          #############################################
#####################################################################################################
#####################################################################################################
#####################################################################################################
#####################################################################################################
#####################################################################################################
#####################################################################################################
#####################################################################################################
def login_user(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return redirect(reverse('BASE:choose_branch'))
			else:
				return render(request, 'BASE/login.html', {'error_message': ''})
		else:
			return render(request, 'BASE/login.html', {'error_message': ''})
	return render(request, 'BASE/login.html')


def register(request):
	form = UserForm(request.POST or None)
	if form.is_valid():
		user = form.save(commit=False)
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		user.set_password(password)
		user.save()
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return redirect('../')
	context = {"form": form,}
	return render(request, 'BASE/register.html', context)

def logout_user(request):
	logout(request)
	form = UserForm(request.POST or None)
	context = {"form": form,}
	return render(request, 'BASE/login.html', context)