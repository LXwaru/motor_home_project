from django.db import models
from datetime import datetime

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
        return self.name

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
    is_sold = models.BooleanField(default=False)
    sold_date = models.DateField(blank=True, null=True, default=None)
    
    def __str__(self):
        return f"{self.year} {self.model.make.name} {self.model.name} - {self.color}"
    
    