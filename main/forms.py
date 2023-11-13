from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Announcement, BlogPost, ExpenseReport
from account.models import Employee


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content']


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
                  "salary",
                  "can_announce",
                  "can_blog",
                  ]
        labels = {'username': "Username",
                  'email': "Email",
                  'first_name': "First Name",
                  'last_name': "Last Name",
                  'address': "Home Address",
                  'phone': "Phone Number",
                  'postal_code': "Postal Code",
                  'salary': "Salary",
                  'can_announce': "Post Announcements?",
                  'can_blog': "Post Blogs?"
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
                  "salary",
                  "can_announce",
                  "can_blog",
                  ]
        labels = {'username': "Username",
                  'email': "Email",
                  'first_name': "First Name",
                  'last_name': "Last Name",
                  'address': "Home Address",
                  'phone': "Phone Number",
                  'postal_code': "Postal Code"
                  'salary': "Salary",
                  'can_announce': "Post Announcements?",
                  'can_blog': "Post Blogs?"
                  }


class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'content']

class ExpenseReportForm(forms.ModelForm):
    class Meta:
        model = ExpenseReport
        fields = ['detail', 'amount', 'photo']
