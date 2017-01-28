from django.contrib.auth import authenticate, login, logout
from django.template import loader
from datetime import date,datetime
from django.urls import reverse
from django import forms
from .models import *
from .forms import *
from django.shortcuts import render,get_object_or_404,redirect

# Create your views here.
def index(request):
	if not request.user.is_authenticated():
		return render(request, 'BASE/login.html')
	else:
		return render(request,"BASE/index.html")

def system_setting(request):
	if not request.user.is_authenticated():
		return render(request, 'BASE/login.html')
	else:
		return render(request, "BASE/system_setting.html")

def add_category(request):
	if not request.user.is_authenticated():
		return render(request, 'BASE/login.html')
	else:
		all_categories = Item_Category.objects.all()
		form = Item_Category_Form(request.POST or None)
		if form.is_valid():
			cat = form.save(commit=False)
			cat.save()
			context = {"form":form,"all_categories":all_categories}
			return render(request,'BASE/add_category.html',context)
		context = {"form":form,"all_categories":all_categories}
		return render(request,'BASE/add_category.html',context)

def add_product(request):
	if not request.user.is_authenticated():
		return render(request, 'BASE/login.html')
	else:
		all_categories = Item.objects.all()
		form = Item_Form(request.POST or None)
		if form.is_valid():
			cat = form.save(commit=False)
			cat.save()
			context = {"form":form,"all_categories":all_categories}
			return render(request,'BASE/add_product.html',context)
		context = {"form":form,"all_categories":all_categories}
		return render(request,'BASE/add_product.html',context)


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
				return render(request, 'BASE/login.html', {'error_message': 'Your account has been disabled'})
		else:
			return render(request, 'BASE/login.html', {'error_message': 'Invalid login'})
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