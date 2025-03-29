from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Employee(AbstractUser):
    full_name = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(max_length=255, unique=True, null=False, blank=False)
    password = models.CharField(max_length=255, null=False, blank=False)
    phone_number = models.CharField(max_length=255, null=False, blank=False)
    address = models.CharField(max_length=255, null=False, blank=False)
    city = models.CharField(max_length=255, null=False, blank=False)
    state = models.CharField(max_length=255, null=False, blank=False)
    zip_code = models.CharField(max_length=255, null=False, blank=False)
    is_service_provider = models.BooleanField(default=False)
    is_sales_person = models.BooleanField(default=False)
    is_service_admin = models.BooleanField(default=False)
    is_sales_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    # Add related_name attributes to resolve the clash
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='employee_set',
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='employee_set',
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'full_name']

    def __str__(self):
        return self.username
    
    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.email
        super().save(*args, **kwargs)

class Customer(models.Model):
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    