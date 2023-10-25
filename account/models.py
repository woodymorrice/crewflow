from django.db import models
from django.contrib.auth.models import Group


# Create your models here.
class EmployeeGroup(Group):
    pass

class ManagerGroup(Group):
    pass
