from django.db import models

class DeliveryBoyDetails(models.Model):
    vendor = models.ForeignKey('owner.Vendor', on_delete=models.CASCADE, to_field='id')
    name = models.CharField(max_length=100,unique=True)
    phone = models.CharField(max_length=15)
    vehicle_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class Salary(models.Model):
    name = models.ForeignKey(DeliveryBoyDetails, on_delete=models.CASCADE, to_field='name')
    date = models.DateField()
    no_of_deliveries = models.IntegerField()
    total_salary = models.FloatField(default=0.0)
    

