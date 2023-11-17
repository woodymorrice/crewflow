from django.conf import settings
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


# class Employee(models.Model):
# address = models.CharField(max_length=255)
# phone = models.CharField(max_length=20)
# position = models.CharField(max_length=255)
# date_of_employment = models.DateTimeField(auto_now_add=True)
# postal_code = models.CharField(max_length=10)

# def __str__(self):
# return self.first_name + self.last_name


# class Manager(Employee):
# pass


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(Employee, on_delete=models.RESTRICT)
    date_added = models.DateTimeField(auto_now_add=True)
    thumbs_up = models.IntegerField(default=0)
    thumbs_down = models.IntegerField(default=0)

class Comment(models.Model):
    to_reply = models.IntegerField(null=True, blank=True)
    content = models.TextField()
    author = models.ForeignKey(Employee, on_delete=models.RESTRICT)
    date_added = models.DateTimeField(auto_now_add=True)
    thumbs_up = models.IntegerField(default=0)
    thumbs_down = models.IntegerField(default=0)
    def __str__(self):
        return f"Comment by {self.author} on Post {self.to_reply or 'main post'}"


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


class TimeOffRequest(models.Model):
    # Fields necessary for the request form
    employee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='time_off_requests'
    )
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.CharField(max_length=200)
    details = models.TextField()

    # The status of the Request
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('denied', 'Denied')
    ]

    # Set the default status to pending
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='pending'
    )

    def __str__(self):
        return f"{self.employee}'s time-off request from {self.start_date} to {self.end_date}"
