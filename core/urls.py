from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('analytics/', views.analytics, name="analytics"),

    path('customers/', views.customers, name="customers"),   
    path('addcustomer/', views.addcust, name="addcustomer"),   
    path('delcust/<int:id>', views.delcust, name="delcust"),   
    path('updatecust/<int:id>', views.updatecust, name = 'updatecust'),
       
    path('delord/<int:id>', views.delord, name = 'delord'),    
]