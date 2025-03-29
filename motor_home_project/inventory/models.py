from django.db import models
from datetime import datetime
from accounts.models import Customer

# Create your models here.
class Make(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Model(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    make_id = models.ForeignKey(Make, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.make_id.name} - {self.name}"
    
    class Meta:
        ordering = ['make_id__name', 'name']

class MotorHome(models.Model):
    id = models.AutoField(primary_key=True)
    vin = models.CharField(max_length=17, unique=True)
    year = models.IntegerField()
    mileage = models.IntegerField(null=True, blank=True, default=None)
    condition = models.CharField(max_length=100, null=True, blank=True, default=None)
    model_id = models.ForeignKey(Model, on_delete=models.CASCADE)
    color = models.CharField(max_length=100)
    ticket_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=None)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    is_new = models.BooleanField(default=True)
    for_sale = models.BooleanField(default=True)
    for_service = models.BooleanField(default=False)
    for_rental = models.BooleanField(default=False)
    is_sold = models.BooleanField(default=False)
    sold_date = models.DateField(blank=True, null=True, default=None)
    owner = models.ForeignKey(
        Customer, 
        on_delete=models.CASCADE,
        related_name="owner",
        null=True,
        blank=True
    )
    
    def __str__(self):
        return f"{self.year} {self.model_id.make_id.name} {self.model_id.name} - {self.color}"
    
    