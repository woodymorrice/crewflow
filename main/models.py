from django.db import models

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



class Person(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    dateOfEmployment = models.DateField(auto_now=False, auto_now_add=False)
    postalCode = models.CharField(max_length=10)

    def __str__(self):
        return self.name