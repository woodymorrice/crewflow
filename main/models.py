from django.db import models
from django.contrib.auth.models import User

# Models/Classes
class Announcement(models.Model):
    title = models.CharField(max_length=255)
    # update this to reflect the user who created it
    author = models.CharField(max_length=255, default="Management")
    # auto_now_add records date+time when created
    date_added = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE);
    first_name = models.CharField(max_length=24)
    last_name = models.CharField(max_length=24)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    dateOfEmployment = models.DateField(auto_now=False, auto_now_add=False)
    postalCode = models.CharField(max_length=10)

#    first_name = models.CharField(max_length=24);
#    last_name = models.CharField(max_length=24);
#    email = models.CharField(max_length=32);

    def __str__(self):
        return self.name
        #return self.first_name + self.last_name

class Manager(Employee):
    pass


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
