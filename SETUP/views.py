# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate, login, logout
from django.template import loader
from datetime import date,datetime
from django.urls import reverse
from django import forms
from BASE.models import *
from .forms import *
from django.shortcuts import render,get_object_or_404,redirect

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']
# Create your views here.
def setup_index(request):
	users = User.objects.all()
	if users.count() < 1:
		form1 = User_Form(request.POST or None)
		form2 = Admin_Form(request.POST or None)
		form3 = Branch_Form(request.POST or None)
		form4 = System_Form(request.POST or None, request.FILES or None)
		if form1.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid():
			new_user = form1.save(commit = False)
			new_user.username = request.POST.get('username')
			new_user.is_staff = True
			password = request.POST.get('password')
			new_user.set_password(password)
			new_admin = form2.save(commit = False)
			new_admin.credit = 0
			new_branch = form3.save(commit = False)
			new_warehouse = Warehouse()
			new_warehouse.name = request.POST.get('name')
			new_warehouse.location = request.POST.get('address')
			new_branch_stock = Branch_Stock()
			new_system = form4.save(commit = False)
			new_system.company_logo = request.FILES['company_logo']
			file_type = new_system.company_logo.url.split('.')[-1]
			file_type = file_type.lower()
			if file_type not in IMAGE_FILE_TYPES:
				context={"error_message":'Image file must be PNG, JPG, or JPEG',"form":form}
				return render(request,'SETUP/setup.html',context)
			new_user.save()
			new_admin.user = new_user
			new_admin.save()
			new_branch.save()
			new_warehouse.save()
			new_branch_stock.branch = new_branch
			new_branch_stock.warehouse = new_warehouse
			new_branch_stock.save()
			new_system.save()
			return redirect(reverse('BASE:login_user'))
		context = {
			"form1":form1,
			'form2':form2,
			'form3':form3,
			'form4':form4,
		}
		return render(request,'SETUP/setup.html',context)
	else:
		return render(request,'BASE/forbidden.html')


