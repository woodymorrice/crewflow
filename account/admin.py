from django.contrib import admin
from django.contrib.auth.models import Group
from .models import EmployeeGroup, ManagerGroup

# Register your models here.

admin.site.unregister(Group)

@admin.register(EmployeeGroup)
class EmployeeGroupAdmin(admin.ModelAdmin):
    pass

@admin.register(ManagerGroup)
class ManagerGroupAdmin(admin.ModelAdmin):
    pass
