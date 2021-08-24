from django.db import models

class Customer(models.Model):
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name

class Product(models.Model):
	name = models.CharField(max_length=200, null=True)
	description = models.CharField(max_length=200, blank=True)
	price = models.IntegerField(null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name

class Order(models.Model):
	STATUS = (
		('In Transit', 'In Transit'),
		('Delivered', 'Delivered'),
		('Processing', 'Processing'),
	)
	Customer = models.ForeignKey(Customer, null=True, on_delete= models.CASCADE)
	Product = models.ManyToManyField(Product, blank=False)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)

	def __str__(self):
		return self.Customer.name