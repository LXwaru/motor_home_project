from django.db import models
from inventory.models import MotorHome
# Create your models here.
class ServicePerson(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class ServiceTicket(models.Model):
    id = models.AutoField(primary_key=True)
    motor_home = models.ForeignKey(MotorHome, on_delete=models.CASCADE)
    service_person = models.ForeignKey(ServicePerson, on_delete=models.CASCADE)
    service_start_date = models.DateField()
    service_end_date = models.DateField(null=True, blank=True, default=None)
    service_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_completed = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)
    is_warranty = models.BooleanField(default=False)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.motor_home.year} - {self.motor_home.model_id.make_id.name} {self.motor_home.model_id.name}, {self.motor_home.color}"
    
class ServiceItem(models.Model):
    id = models.AutoField(primary_key=True)
    item_description = models.TextField(blank=True, null=True)
    item_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    service_ticket = models.ForeignKey(
        ServiceTicket, 
        on_delete=models.CASCADE,
        related_name='items'
    )
    
    def __str__(self):
        return f"{self.item_description} - {self.item_price}"
    
