from django.shortcuts import render
from django.http import HttpResponse
from django.db import IntegrityError
from .models import DeliveryBoyDetails, Salary


# Create your views here.
def vendorcheck(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        name = request.POST.get('username')
        password = request.POST.get('password')

        from owner.models import Vendor
        try:
            vendor = Vendor.objects.get(name=name, password=password)
            delivery_boys = DeliveryBoyDetails.objects.filter(vendor_id=vendor.id)
            return render(request, 'vendor_dash.html', {'vendor': vendor, 'delivery_boys': delivery_boys})
        except Vendor.DoesNotExist:
            return HttpResponse("Invalid credentials")

def vendor_dash(request, v_id):
    from owner.models import Vendor
    vendor = Vendor.objects.get(id=v_id)
    delivery_boys = DeliveryBoyDetails.objects.filter(vendor_id=v_id)
    return render(request, 'vendor_dash.html', {'vendor': vendor, 'delivery_boys': delivery_boys})

def add_delivery_boy(request, vendor_id):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        vehicle_number = request.POST.get('vehicle_number')

        delivery_boy = DeliveryBoyDetails(
            vendor_id=vendor_id,
            name=name,
            phone=phone,
            vehicle_number=vehicle_number
        )
        try:
            delivery_boy.save()
            from django.shortcuts import redirect
            return redirect('vendor_dash', v_id=vendor_id)
        except IntegrityError:
            return render(request, 'add_delivery_boy.html', {'vendor_id': vendor_id, 'error': 'Name already exists'})
    else:
        return render(request, 'add_delivery_boy.html', {'vendor_id': vendor_id})


def edit_delivery_boy(request, vendor_id, name):
    delivery_boy = DeliveryBoyDetails.objects.get(vendor_id=vendor_id, name=name)
    if request.method == 'POST':
        new_name = request.POST.get('name')
        phone = request.POST.get('phone')
        vehicle_number = request.POST.get('vehicle_number')

        # Check if new name is unique, but allow if it's the same
        if new_name != delivery_boy.name and DeliveryBoyDetails.objects.filter(name=new_name).exists():
            return render(request, 'edit_delivery_boy.html', {'delivery_boy': delivery_boy, 'vendor_id': vendor_id, 'error': 'Name already exists'})

        delivery_boy.name = new_name
        delivery_boy.phone = phone
        delivery_boy.vehicle_number = vehicle_number
        try:
            delivery_boy.save()
            from django.shortcuts import redirect
            return redirect('vendor_dash', v_id=vendor_id)
        except IntegrityError:
            return render(request, 'edit_delivery_boy.html', {'delivery_boy': delivery_boy, 'vendor_id': vendor_id, 'error': 'Error updating delivery boy'})
    else:
        return render(request, 'edit_delivery_boy.html', {'delivery_boy': delivery_boy, 'vendor_id': vendor_id})

def delete_delivery_boy(request, vendor_id, name):
    delivery_boy = DeliveryBoyDetails.objects.get(vendor_id=vendor_id, name=name)
    delivery_boy.delete()  # This will cascade delete salaries
    from django.shortcuts import redirect
    return redirect('vendor_dash', v_id=vendor_id)

def info(request, vendorid , name):
    vendor = DeliveryBoyDetails.objects.get(vendor_id=vendorid, name=name)

    if request.method == 'POST':
        date = request.POST.get('date')
        no_of_deliveries = request.POST.get('no_of_deliveries')
        # Assume total_salary is no_of_deliveries * 100, for example
        total_salary = int(no_of_deliveries) * 10 if no_of_deliveries else 0
        salary, created = Salary.objects.get_or_create(
            name=vendor,
            date=date,
            defaults={'no_of_deliveries': no_of_deliveries, 'total_salary': total_salary}
        )
        if not created:
            salary.no_of_deliveries = no_of_deliveries
            salary.total_salary = total_salary
            salary.save()

    return render(request, 'info.html',{'db':vendor})

