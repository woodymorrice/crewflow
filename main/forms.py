from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Announcement, BlogPost, ExpenseReport, TimeOffRequest, Comment
from account.models import Employee


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content']


class BlogCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']


class AddEmployeeForm(UserCreationForm):
    class Meta:
        model = Employee
        fields = ["username",
                  "first_name",
                  "last_name",
                  "email",
                  "address",
                  "phone",
                  "postal_code",
                  "can_announce",
                  "can_blog",
                  "salary",
                  ]
        labels = {'username': "Username",
                  'email': "Email",
                  'first_name': "First Name",
                  'last_name': "Last Name",
                  'address': "Home Address",
                  'phone': "Phone Number",
                  'postal_code': "Postal Code",
                  'can_announce': "Post Announcements?",
                  'can_blog': "Post Blogs?",
                  'salary': "Salary",
                  }


class ChangeEmployeeForm(UserChangeForm):
    class Meta:
        model = Employee
        fields = ["username",
                  "first_name",
                  "last_name",
                  "email",
                  "address",
                  "phone",
                  "postal_code",
                  "can_announce",
                  "can_blog",
                  "salary",
                  ]
        labels = {'username': "Username",
                  'email': "Email",
                  'first_name': "First Name",
                  'last_name': "Last Name",
                  'address': "Home Address",
                  'phone': "Phone Number",
                  'postal_code': "Postal Code",
                  'can_announce': "Post Announcements?",
                  'can_blog': "Post Blogs?",
                  'salary': "Salary",
                  }


class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'content']

class ExpenseReportForm(forms.ModelForm):
    class Meta:
        model = ExpenseReport
        fields = ['detail', 'amount', 'photo']

class TimeOffRequestForm(forms.ModelForm):
    class Meta:
        model = TimeOffRequest
        fields = ['start_date',
                  'end_date',
                  'reason',
                  'details',]
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'reason': forms.Select(choices=TimeOffRequest.STATUS_CHOICES)
        }
