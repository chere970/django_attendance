from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    ADMIN = 'admin'
    EMPLOYEE = 'employee'
    MANAGER = 'manager'
    ROLE_CHOICES = (
        (ADMIN, 'ADMIN'),
        (EMPLOYEE, 'EMPLOYEE'),
        (MANAGER, 'MANAGER')
    )
    # models.CharField(max_length=20, choices=ROLE_CHOICES, default=EMPLOYEE)
    name = models.CharField(max_length=200, null=True)
    username = models.CharField(max_length=200, unique=True)
    employee_id = models.CharField(max_length=100, unique=True, null=True)
    email = models.EmailField(unique=True, null=True)
    role = models.CharField(
        max_length=20, choices=ROLE_CHOICES, default=EMPLOYEE)
    department = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=200)
    # profilephoto = models.ImageField(null=True, blank=True, upload_to='profiles/', default="profiles/default.png")
