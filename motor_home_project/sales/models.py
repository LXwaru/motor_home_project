from django.db import models
from inventory.models import MotorHome

# Create your models here.
class SalesPerson(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    commission_rate = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Sale(models.Model):
    id = models.AutoField(primary_key=True)
    motor_home = models.ForeignKey(MotorHome, on_delete=models.CASCADE)
    sales_person = models.ForeignKey(SalesPerson, on_delete=models.CASCADE)
    sale_date = models.DateField()
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    on_hold = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)
    warranty_end_date = models.DateField(null=True, blank=True, default=None)
    
    def __str__(self):
        return f"{self.motor_home.year} {self.motor_home.model.name} {self.motor_home.color} - {self.sale_date}"
    
    

