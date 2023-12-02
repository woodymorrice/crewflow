from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from main.forms import AddEmployeeForm, ChangeEmployeeForm, AvailabilityForm, ChangeAvailabilityForm, ScheduleCreationForm
from .models import Employee
from main.models import Availability, Schedule

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
                    "salary",
                    "deduction",
                    "payroll_status",
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
admin.site.register(Availability)
admin.site.register(Schedule)
admin.site.unregister(Group)
