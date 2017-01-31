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
			all_entries = Item_Category.objects.all()
			form = Item_Category_Form(request.POST or None)
			if form.is_valid():
				cat = form.save(commit=False)
				cat.save()
				context = {"form":form,"all_entries":all_entries}
				return render(request,'BASE/add_category.html',context)
			context = {"form":form,"all_entries":all_entries}
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
				return redirect('../')
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