from django.db import models

# Create your models here.
class Make(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class ModelVehicle(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    make = models.ForeignKey(Make, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class MotorHome(models.Model):
    id = models.AutoField(primary_key=True)
    vin = models.CharField(max_length=17, unique=True)
    year = models.IntegerField()
    model = models.ForeignKey(ModelVehicle, on_delete=models.CASCADE)
    color = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='motor_homes/', null=True, blank=True)
    is_new = models.BooleanField(default=True)
    for_sale = models.BooleanField(default=True)
    is_sold = models.BooleanField(default=False)
    sold_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.year} {self.model.make.name} {self.model.name} - {self.color}"
    
    