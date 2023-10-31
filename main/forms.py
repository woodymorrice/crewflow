from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Announcement, BlogPost, Employee


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'author']


class AddEmployeeForm(UserCreationForm):
    class Meta:
        model = Employee
        fields = ["first_name",
                  "last_name",
                  "address",
                  "phone",
                  "email",
                  "postal_code"]
        labels = {'first_name': "First Name",
                  'last_name': "Last Name",
                  'address': "Home Address",
                  'phone': "Phone Number",
                  'email': "Email Address",
                  'postal_code': "Postal Code"}

class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'content']
