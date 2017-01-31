from django.contrib.auth import authenticate, login, logout
from django.template import loader
from datetime import date,datetime
from django.urls import reverse
from django import forms
from .models import *
from BASE.models import *
from POS.models import *
from DELIVERY.models import *
from PURCHASES.models import *
#from .forms import *
from django.shortcuts import render,get_object_or_404,redirect

# Create your views here.

def reports_index(request):
	if not request.user.is_authenticated():
		return render(request,'BASE/login.html')
	else:
		return render(request,"REPORTS/home.html")

def this_day(request):
	this_day = datetime.today()
	all_pos_inv = POS_Invoice.objects.filter()
	all_delivery_inv = Delivery_Invoice.objects.all()
	all_purchases_inv = Purchase_Invoice.objects.all()
	all_expenses = Expense_Transaction.objects.all()
	pos_today_inv = []
	pos_total_report = 0
	delivery_today_inv = []
	delivery_total_report = 0
	purchases_today_inv = []
	purchases_total_report = 0
	expenses_today_inv = []
	expenses_total_report = 0

	for x in all_pos_inv:
		this_inv_total = 0
		if x.date.month == this_day.month and x.date.year == this_day.year and x.date.day == this_day.day:
			z = x.get_items()
			for y in z:
				this_inv_total += y.total_price
			pos_today_inv.append((x,this_inv_total))
			pos_total_report += this_inv_total

	for x in all_delivery_inv:
		this_inv_total = 0
		if x.date.month == this_day.month and x.date.year == this_day.year and x.date.day == this_day.day:
			z = x.get_items()
			for y in z:
				this_inv_total += y.total_price
			delivery_today_inv.append((x,this_inv_total))
			delivery_total_report += this_inv_total

	for x in all_purchases_inv:
		this_inv_total = 0
		if x.date.month == this_day.month and x.date.year == this_day.year and x.date.day == this_day.day:
			z = x.get_items()
			for y in z:
				this_inv_total += y.total_price
			purchases_today_inv.append((x,this_inv_total))
			purchases_total_report += this_inv_total
	for x in all_expenses:
		this_inv_total = 0
		if x.date.month == this_day.month and x.date.year == this_day.year and x.date.day == this_day.day:
			expenses_today_inv.append((x,x.amount))
			expenses_total_report += x.amount

	context = {
		'pos_today_inv':pos_today_inv,'pos_total_report':pos_total_report,
		"delivery_today_inv":delivery_today_inv,"delivery_total_report":delivery_total_report,
		"purchases_today_inv":purchases_today_inv,"purchases_total_report":purchases_total_report,
		"expenses_today_inv":expenses_today_inv,"expenses_total_report":expenses_total_report,
		}
	return render(request,'REPORTS/today.html',context)


def this_month(request):
	this_day = datetime.today()
	all_pos_inv = POS_Invoice.objects.all()
	all_delivery_inv = Delivery_Invoice.objects.all()
	all_purchases_inv = Purchase_Invoice.objects.all()
	all_expenses = Expense_Transaction.objects.all()
	pos_today_inv = []
	pos_total_report = 0
	delivery_today_inv = []
	delivery_total_report = 0
	purchases_today_inv = []
	purchases_total_report = 0
	expenses_today_inv = []
	expenses_total_report = 0

	for x in all_pos_inv:
		this_inv_total = 0
		if x.date.month == this_day.month and x.date.year == this_day.year:
			z = x.get_items()
			for y in z:
				this_inv_total += y.total_price
			pos_today_inv.append((x,this_inv_total))
			pos_total_report += this_inv_total

	for x in all_delivery_inv:
		this_inv_total = 0
		if x.date.month == this_day.month and x.date.year == this_day.year:
			z = x.get_items()
			for y in z:
				this_inv_total += y.total_price
			delivery_today_inv.append((x,this_inv_total))
			delivery_total_report += this_inv_total

	for x in all_purchases_inv:
		this_inv_total = 0
		if x.date.month == this_day.month and x.date.year == this_day.year:
			z = x.get_items()
			for y in z:
				this_inv_total += y.total_price
			purchases_today_inv.append((x,this_inv_total))
			purchases_total_report += this_inv_total
	for x in all_expenses:
		this_inv_total = 0
		if x.date.month == this_day.month and x.date.year == this_day.year:
			expenses_today_inv.append((x,x.amount))
			expenses_total_report += x.amount

	context = {
		'pos_today_inv':pos_today_inv,'pos_total_report':pos_total_report,
		"delivery_today_inv":delivery_today_inv,"delivery_total_report":delivery_total_report,
		"purchases_today_inv":purchases_today_inv,"purchases_total_report":purchases_total_report,
		"expenses_today_inv":expenses_today_inv,"expenses_total_report":expenses_total_report,
		}
	return render(request,'REPORTS/today.html',context)


def this_year(request):
	this_day = datetime.today()
	all_pos_inv = POS_Invoice.objects.all()
	all_delivery_inv = Delivery_Invoice.objects.all()
	all_purchases_inv = Purchase_Invoice.objects.all()
	all_expenses = Expense_Transaction.objects.all()
	pos_today_inv = []
	pos_total_report = 0
	delivery_today_inv = []
	delivery_total_report = 0
	purchases_today_inv = []
	purchases_total_report = 0
	expenses_today_inv = []
	expenses_total_report = 0

	for x in all_pos_inv:
		this_inv_total = 0
		if x.date.year == this_day.year:
			z = x.get_items()
			for y in z:
				this_inv_total += y.total_price
			pos_today_inv.append((x,this_inv_total))
			pos_total_report += this_inv_total

	for x in all_delivery_inv:
		this_inv_total = 0
		if x.date.year == this_day.year:
			z = x.get_items()
			for y in z:
				this_inv_total += y.total_price
			delivery_today_inv.append((x,this_inv_total))
			delivery_total_report += this_inv_total

	for x in all_purchases_inv:
		this_inv_total = 0
		if x.date.year == this_day.year:
			z = x.get_items()
			for y in z:
				this_inv_total += y.total_price
			purchases_today_inv.append((x,this_inv_total))
			purchases_total_report += this_inv_total
	for x in all_expenses:
		this_inv_total = 0
		if x.date.year == this_day.year:
			expenses_today_inv.append((x,x.amount))
			expenses_total_report += x.amount

	context = {
		'pos_today_inv':pos_today_inv,'pos_total_report':pos_total_report,
		"delivery_today_inv":delivery_today_inv,"delivery_total_report":delivery_total_report,
		"purchases_today_inv":purchases_today_inv,"purchases_total_report":purchases_total_report,
		"expenses_today_inv":expenses_today_inv,"expenses_total_report":expenses_total_report,
		}
	return render(request,'REPORTS/today.html',context)