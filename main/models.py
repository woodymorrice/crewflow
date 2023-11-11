from django.db import models
from account.models import Employee

# Models/Classes
class Announcement(models.Model):
    title = models.CharField(max_length=255)
    # update this to reflect the user who created it
    author = models.ForeignKey(Employee, on_delete=models.RESTRICT)
    # auto_now_add records date+time when created
    date_added = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.title

class AnnouncementReadStatus(models.Model):
    user = models.ForeignKey(Employee, on_delete=models.CASCADE)
    announcement = models.ForeignKey(Announcement, on_delete=models.CASCADE)
    read = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'announcement')

#class Employee(models.Model):
    #address = models.CharField(max_length=255)
    #phone = models.CharField(max_length=20)
    #position = models.CharField(max_length=255)
    #date_of_employment = models.DateTimeField(auto_now_add=True)
    #postal_code = models.CharField(max_length=10)

    #def __str__(self):
        #return self.first_name + self.last_name


#class Manager(Employee):
    #pass


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Employee, on_delete=models.RESTRICT)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)


class ExpenseReport(models.Model):
    requester = models.ForeignKey(Employee, on_delete=models.CASCADE)
    detail = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to='expense_reports/')
    date_submitted = models.DateTimeField(auto_now_add=True)

    class Status(models.TextChoices):
        IN_PROCESS = "IN_PROCESS", 'In Process'
        APPROVED = "APPROVED", 'Approved'
        DECLINED = "DECLINED", 'Declined'

    status = models.CharField(max_length=24, choices=Status.choices, default=Status.IN_PROCESS)

    def __str__(self):
        return f'{self.requester.username} - {self.date_submitted}'

