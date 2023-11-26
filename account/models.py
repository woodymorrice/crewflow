from django.db import models
from django.contrib.auth.models import AbstractUser


class Employee(AbstractUser):
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    position = models.CharField(max_length=255)
    date_of_employment = models.DateTimeField(auto_now_add=True)
    postal_code = models.CharField(max_length=10)
    can_announce = models.BooleanField(default=False)
    can_blog = models.BooleanField(default=False)
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    deduction = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    class Role(models.TextChoices):
        ADMIN = "ADMIN", 'Admin'
        MANAGER = "MANAGER", 'Manager'
        EMPLOYEE = "EMPLOYEE", "Employee"

    base_role = Role.EMPLOYEE

    role = models.CharField(max_length=24, choices=Role.choices)

    def save(self, *arg, **kwargs):
        # if not self.pk:
        #     self.role = self.base_role
        return super().save(*arg, **kwargs)

    def is_manager(self):
        return self.role == self.Role.MANAGER
