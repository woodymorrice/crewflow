from django import forms
from .models import BlogPost
from .models import Person


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'author']


class AddEmployee(forms.ModelForm):
    class Meta:
        model = Person

        fields = ["name",
                  "address",
                  "phone",
                  "email",
                  "position",
                  "dateOfEmployment",
                  "postalCode"]
        labels = {'name': "Employee Full Name",
                  'address': "Employee Home Address",
                  'phone': "Employee Phone Number",
                  'email': "Employee Email Address",
                  'position': "Position of Employee",
                  'dateOfEmployment': "Date of Employment",
                  'postalCode': "Employee Postal Code"}

