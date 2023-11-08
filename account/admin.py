from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from main.forms import AddEmployeeForm, ChangeEmployeeForm
from .models import Employee

class EmployeeAdmin(UserAdmin):
    add_form = AddEmployeeForm
    form = ChangeEmployeeForm
    model = Employee
    fieldsets = (
        (None, 
            {
                "fields": (
                    "username",
                    "password",
                ),
            },
        ),
        (("Personal info"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "position",
                    "email",
                    "phone",
                    "address",
                    "postal_code",
                ),
            },
        ),
        (("Permissions"),
            {
                "fields": (
                    "role",
                    "can_announce",
                    "can_blog",
                    "is_superuser",
                ),
            },
        ),
        (("Important dates"),
            {
                "fields": (
                    "date_joined",
                ),
            },
        ),
    )

# Register your models here.
admin.site.register(Employee, EmployeeAdmin)
admin.site.unregister(Group)
