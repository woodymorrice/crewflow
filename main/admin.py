from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from account.models import User

# Here we define what models can be
# managed by the administrator

# Import the model
from .models import Announcement, Employee, Manager

# These models allow the extra user information
# to be viewable from the admin panel
class EmployeeInline(admin.StackedInline):
    model = Employee
    can_delete = False
    verbose_name_plural = "employee"


class UserAdmin(BaseUserAdmin):
    inlines = [EmployeeInline]

# register the model using this function
admin.site.register(Announcement)
admin.site.register(User, UserAdmin)
