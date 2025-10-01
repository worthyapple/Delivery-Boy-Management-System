

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def adminlogin(request):
    return render(request, 'adminlogin.html')

def vendorlogin(request):
    return render(request, 'vendorlogin.html')