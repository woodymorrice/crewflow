from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import Employee

from .forms import AddEmployeeForm, ChangeEmployeeForm

# Here we define what models can be
# managed by the administrator

# Import the model
from .models import Announcement

# These models allow the extra user information
# to be viewable from the admin panel
#class EmployeeInline(admin.StackedInline):
    #model = Employee
    #can_delete = False


#class UserAdmin(BaseUserAdmin):
    #inlines = [EmployeeInline]

#class EmployeeAdmin(UserAdmin):
#    add_form = AddEmployeeForm
#    form = ChangeEmployeeForm
#    model = Employee

# register the model using this function
admin.site.register(Announcement)
#admin.site.register(Employee, EmployeeAdmin)
