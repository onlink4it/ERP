from django.contrib.auth import authenticate, login, logout
from django.template import loader
from datetime import date,datetime
from django.urls import reverse
from django import forms
from .models import *
from BASE.models import *
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

# Create your views here.
##################################### For Creating Invoices ########################################
def POS_home(request):
	if not request.user.is_authenticated():
		return render(request, 'BASE/login.html')
	else:
		if perm(request,request.user,"is_pos_employee") == True or perm(request,request.user,"is_pos_admin") == True:
			check_perm = User_Admin.objects.get(user=request.user)
			pos_employee = False
			pos_admin = False
			if check_perm.is_pos_employee == True :
				pos_employee = True
			if check_perm.is_pos_admin == True:
				pos_admin = True
			all_invoices = POS_Invoice.objects.all()
			all_emp = User_Admin.objects.all()
			pos_employees = []
			for x in all_emp:
				if x.is_pos_admin == True or x.is_pos_employee == True:
					pos_employees.append(x)

			unpaid_invoices = POS_Invoice.objects.filter(is_closed=False)
			all_customers = POS_Customer.objects.all()
			form = POS_Add_Invoice_Form(request.POST or None)
			if form.is_valid():
				x = form.save(commit=False)
				x.date = datetime.now()
				x.save()
				return redirect('../POS/Invoice/' + str(x.id) + '/Categories/' , inv_id = x.id)
			context = {
				"form":form,
				"all_customers":all_customers,
				"unpaid_invoices":unpaid_invoices,
				"all_invoices":all_invoices,
				"pos_employee":pos_employee,
				"pos_admin":pos_admin,
				"pos_employees":pos_employees,
				}
			return render(request,'POS/home.html',context)
		else:
			return render(request,'BASE/forbidden.html')


###############################################################################################	
###############################################################################################	
###############################################################################################	
###############################################################################################	
###############################################################################################	
###############################################################################################	
######################################   INV Management     #######################################	
###############################################################################################	
###############################################################################################	
###############################################################################################	
###############################################################################################	
###############################################################################################	
###############################################################################################	
###############################################################################################	
###############################################################################################	
##################################### For Categories View ########################################

def POS_categories(request,inv_id):
	if not request.user.is_authenticated():
		return render(request,'BASE/login.html')
	else:
		if perm(request,request.user,"is_pos_employee") == True or perm(request,request.user,"is_pos_admin") == True:
			all_cat = Item_Category.objects.all()
			inv_items = POS_Invoice_Items.objects.filter(invoice=inv_id)
			this_inv = POS_Invoice.objects.get(id=inv_id)
			opened_inv = POS_Invoice.objects.filter(is_closed =False)
			context={'all_cat':all_cat,"inv_items":inv_items,"inv_id":inv_id,"this_inv":this_inv,"opened_inv":opened_inv}
			return render(request,'POS/categories.html',context)
		else:
			return render(request,'BASE/forbidden.html')

##################################### For All Category Products View ########################################
def POS_items(request,inv_id,cat_id):
	if not request.user.is_authenticated():
		return render(request,'BASE/login.html')
	else:
		if perm(request,request.user,"is_pos_employee") == True or perm(request,request.user,"is_pos_admin") == True:
			all_items = Item.objects.filter(category = cat_id)
			inv_items = POS_Invoice_Items.objects.filter(invoice=inv_id)
			this_inv = POS_Invoice.objects.get(id=inv_id)
			opened_inv = POS_Invoice.objects.filter(is_closed =False)
			context={'all_items':all_items,"inv_items":inv_items,"inv_id":inv_id,"this_inv":this_inv,"opened_inv":opened_inv}
			return render(request,'POS/items.html',context)
		else:
			return render(request,'BASE/forbidden.html')

##################################### For Adding Item To Invoices ########################################
def POS_add_item(request,inv_id,item_id):
	if not request.user.is_authenticated():
		return render(request,'BASE/login.html')
	else:
		if perm(request,request.user,"is_pos_employee") == True or perm(request,request.user,"is_pos_admin") == True:
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
		else:
			return render(request,'BASE/forbidden.html')

##################################### For Increasing Quantity of an item ########################################
def POS_increase_quantity(request,inv_id,inv_item_id):
	if not request.user.is_authenticated():
		return render(request,'BASE/login.html')
	else:
		if perm(request,request.user,"is_pos_employee") == True or perm(request,request.user,"is_pos_admin") == True:
			selected_item = POS_Invoice_Items.objects.get(pk=inv_item_id)
			selected_item.quantity += 1
			selected_item.total_price += selected_item.unit_price
			selected_item.save()
			return redirect('../../Categories/')
		else:
			return render(request,'BASE/forbidden.html')



def POS_decrease_quantity(request,inv_id,inv_item_id):
	if not request.user.is_authenticated():
		return render(request,'BASE/login.html')
	else:
		if perm(request,request.user,"is_pos_employee") == True or perm(request,request.user,"is_pos_admin") == True:
			selected_item = POS_Invoice_Items.objects.get(pk=inv_item_id)
			selected_item.quantity -= 1
			selected_item.total_price -= selected_item.unit_price
			selected_item.save()
			return redirect('../../Categories/')
		else:
			return render(request,'BASE/forbidden.html')

def POS_delete_invoice_item(request,inv_id,inv_item_id):
	if not request.user.is_authenticated():
		return render(request,'BASE/login.html')
	else:
		if perm(request,request.user,"is_pos_employee") == True or perm(request,request.user,"is_pos_admin") == True:
			selected_item = POS_Invoice_Items.objects.get(pk=inv_item_id)
			if selected_item.is_closed == False:
				selected_item.delete()
				return redirect('../../Categories/')
			else:
				return render(request,'BASE/forbidden.html')
		else:
			return render(request,'BASE/forbidden.html')


def POS_delete_invoice(request,inv_id):
	if not request.user.is_authenticated():
		return render(request,'BASE/login.html')
	else:
		if perm(request,request.user,"is_pos_admin") == True:
			selected_invoice = POS_Invoice.objects.get(pk=inv_id)
			selected_invoice.delete()
			return redirect('../../../../')
		else:
			return render(request,'BASE/forbidden.html')


def POS_close_invoice(request,inv_id):
	if not request.user.is_authenticated():
		return render(request,'BASE/login.html')
	else:
		if perm(request,request.user,"is_pos_employee") == True or perm(request,request.user,"is_pos_admin") == True:
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
		else:
			return render(request,'BASE/forbidden.html')

def POS_pay_invoice(request,inv_id):
	if not request.user.is_authenticated():
		return render(request,'BASE/login.html')
	else:
		if perm(request,request.user,"is_pos_employee") == True or perm(request,request.user,"is_pos_admin") == True:
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
		else:
			return render(request,'BASE/forbidden.html')

def POS_print_invoice(request,inv_id):
	if not request.user.is_authenticated():
		return render(request,'BASE/login.html')
	else:
		if perm(request,request.user,"is_pos_employee") == True or perm(request,request.user,"is_pos_admin") == True:
			this_inv = POS_Invoice.objects.get(id=inv_id)		
			if this_inv.is_closed == True:
				inv_items = POS_Invoice_Items.objects.filter(invoice=inv_id)
				inv_total = 0
				for x in inv_items:
					inv_total += x.total_price
				context = {"this_inv":this_inv,"inv_items":inv_items,"inv_total":inv_total}
				return render(request, 'BASE/invoice.html',context)
			else:
				return render(request,'BASE/forbidden.html')
		else:
			return render(request,'BASE/forbidden.html')


def POS_add_customer(request):
	if not request.user.is_authenticated():
		return render(request,'BASE/login.html')
	else:
		if perm(request,request.user,"is_pos_employee") == True or perm(request,request.user,"is_pos_admin") == True:
			all_customers = POS_Customer.objects.all()
			form = POS_CustomerForm(request.POST or None)
			if form.is_valid():
				customer = form.save(commit=False)
				customer.save()
				context = {"all_customers":all_customers}
				return render(request,'POS/add_customer.html',context)
			context = {"form":form,"all_customers":all_customers}
			return render(request,'POS/add_customer.html',context)
		else:
			return render(request,'BASE/forbidden.html')


def POS_delete_customer(request,customer_id):
	if not request.user.is_authenticated():
		return render(request,'BASE/login.html')
	else:
		if  perm(request,request.user,"is_pos_admin") == True:
			this_customer = POS_Customer.objects.get(pk = customer_id)
			this_customer.delete()
			return redirect('/POS/')
		else:
			return render(request,'BASE/forbidden.html')

def POS_customer_payment(request,customer_id):
	if not request.user.is_authenticated():
		return render(request,'BASE/login.html')
	else:
		if perm(request,request.user,"is_pos_employee") == True or perm(request,request.user,"is_pos_admin") == True:
			this_customer = POS_Customer.objects.get(pk = customer_id)
			form = POS_Customer_Payment_Form(request.POST or None)
			if form.is_valid():
				this_emp = User_Admin.objects.get(user = request.user)
				x = form.save(commit = False)
				this_customer.credit += x.amount
				trans = POS_Transactions()
				trans.amount = x.amount
				trans.date = datetime.now()
				trans.customer = this_customer
				trans.comment = "سداد من العميل " + this_customer.name + "الي الموظف " + this_emp.user.username
				this_emp.credit -=x.amount
				this_customer.save()
				this_emp.save()
				trans.save()
				error_message = "تم تسديد المبلغ بنجاح"
				context = {"error_message":error_message}
				return render(request,'POS/customer_payment.html',context)
			context = {"form":form}
			return render(request,'POS/customer_payment.html',context)
		else:
			return render(request,'BASE/forbidden.html')

def POS_employee_payment(request,emp_id):
	if not request.user.is_authenticated():
		return render(request,'BASE/login.html')
	else:
		if  perm(request,request.user,"is_pos_admin") == True:
			this_emp = User_Admin.objects.get(pk = emp_id)
			form = POS_Employee_Payment_Form(request.POST or None)
			if form.is_valid():
				x = form.save(commit = False)
				this_emp.credit += x.amount
				treasury_trans = Treasury()
				treasury_trans.date = datetime.now()
				treasury_trans.amount = x.amount
				treasury_trans.comment = "سداد من موظف الكاشير " + this_emp.user.username
				this_emp.save()
				treasury_trans.save()
				error_message = "تم سداد الموظف بنجاح"
				context = {"error_message":error_message}
				return render(request,'POS/employee_payment.html',context)
			context = {'form':form}
			return render(request,'POS/employee_payment.html',context)
		else:
			return render(request,'BASE/forbidden.html')


