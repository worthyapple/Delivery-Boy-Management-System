from django.shortcuts import render
from django.contrib.auth import authenticate
from django.http import HttpResponse
from .models import Admin, Vendor

# Create your views here.

def admincheck(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            admin = Admin.objects.get(username=username)
            return render(request, 'admin_dashboard.html', {'Vendor': Vendor.objects.all()})
        except Admin.DoesNotExist:
            return HttpResponse("Invalid credentials")
        

        
def vendordashboard(request):
    return render(request, 'vendordashboard.html')

def add_vendor(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        name = request.POST.get('name')
        password = request.POST.get('password')


        vendor = Vendor(id=id, name=name, password=password)
        vendor.save()
        return render(request, 'vendordashboard.html', {'Vendor': Vendor.objects.all()})
    else:
        return render(request, 'add_vendor.html')

def add_admin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')


        admin = Admin(username=username, password=password)
        admin.save()
        return render(request, 'admin_dashboard.html', {'Vendor': Vendor.objects.all()})
    else:
        return render(request, 'add_admin.html')
    

