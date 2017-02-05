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
		