"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from project import views
from owner.views import admincheck,vendordashboard,add_vendor,add_admin
from vendor.views import vendorcheck,info,add_delivery_boy,vendor_dash,edit_delivery_boy,delete_delivery_boy

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('adminlogin',views.adminlogin,name='adminlogin'),
    path('vendorlogin',views.vendorlogin,name='vendorlogin'),
    path('admincheck',admincheck,name='admincheck'),
    path('vendorcheck',vendorcheck,name='vendorcheck'),
    path('add_vendor',add_vendor,name='add_vendor'),
    path('add_admin',add_admin,name='add_admin'),
    path('vendordashboard',vendordashboard,name='vendordashboard'),
    path('vendor_dash/<str:v_id>/', vendor_dash, name='vendor_dash'),
    path('add_delivery_boy/<str:vendor_id>/', add_delivery_boy, name='add_delivery_boy'),
    path('edit_delivery_boy/<str:vendor_id>/<str:name>/', edit_delivery_boy, name='edit_delivery_boy'),
    path('delete_delivery_boy/<str:vendor_id>/<str:name>/', delete_delivery_boy, name='delete_delivery_boy'),
    path('info//<str:vendorid>/<str:name>', info, name='info'),
]
