from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

class CustAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['name', 
    'phone', 
    'email', 
    'date_created']

class ProdAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [        
        'name',
        'price',
        'date_created',
    ]

admin.site.register(Customer, CustAdmin)
admin.site.register(Product, ProdAdmin)
admin.site.register(Order)