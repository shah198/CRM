from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from .models import *
from .forms import *

def home(request):
	orders = Order.objects.all()
	customers = Customer.objects.all()

	totcustomers = customers.count()
	totorders = orders.count()

	delivered = orders.filter(status='Delivered').count()
	processing = orders.filter(status='Processing').count()
	intransit = orders.filter(status='In Transit').count()

	context = {'orders':orders, 'customers':customers, 'totorders':totorders, 'totcustomers':totcustomers, 'delivered':delivered, 'processing':processing, 'intransit':intransit }

	return render(request, 'core/home.html', context)

def customers(request):
	orders = Order.objects.all()
	customers = Customer.objects.all()

	totcustomers = customers.count()
	totorders = orders.count()

	delivered = orders.filter(status='Delivered').count()
	processing = orders.filter(status='Processing').count()
	intransit = orders.filter(status='In Transit').count()

	context = {'orders':orders, 'customers':customers, 'totorders':totorders, 'totcustomers':totcustomers, 'delivered':delivered, 'processing':processing, 'intransit':intransit }

	return render(request, 'core/customers.html', context)

def analytics(request):
    labels = []
    data = []
    queryset = Product.objects.order_by('-price')[:10]
    for prod in queryset:
        labels.append(prod.name)
        data.append(prod.price)

    return render(request, 'core/analytics.html', {
        'labels': labels,
        'data': data,
    })

def delord(request, id):
    order = Order.objects.get(pk=id)
    order.delete()
    return home(request)

def addcust(request):
    fm = CustomerRegistration(request.POST)
    if fm.is_valid():
        cust = Customer.objects.create()
        fm.save()
        return customers(request)
    return render(request, 'core/addcustomer.html', {'form':fm})

def delcust(request, id):
    cust = Customer.objects.get(pk=id)
    cust.delete()
    return customers(request)

def updatecust(request, id):
    name = Customer.objects.get(pk=id)
    if(request.method=='POST'):
        fm = CustomerRegistration(request.POST, instance = name)
        if fm.is_valid():
            fm.save()
            return customers(request)
    else:
        fm = CustomerRegistration(instance = name)
        if fm.is_valid():
            fm.save()
            return customers(request)
    return render(request, 'core/edit.html', {'id':id, 'name':name, 'form':fm})