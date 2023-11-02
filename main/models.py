from django.db import models
from account.models import User

# Models/Classes
class Announcement(models.Model):
    title = models.CharField(max_length=255)
    # update this to reflect the user who created it
    author = models.ForeignKey(User, on_delete=models.RESTRICT)
    # auto_now_add records date+time when created
    date_added = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Employee(User):
    #user = models.OneToOneField(User, on_delete=models.CASCADE);
    #first_name = models.CharField(max_length=24)
    #last_name = models.CharField(max_length=24)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    #email = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    date_of_employment = models.DateTimeField(auto_now_add=True)
    postal_code = models.CharField(max_length=10)

    def __str__(self):
        return self.first_name + self.last_name


class Manager(Employee):
    pass


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.RESTRICT)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

