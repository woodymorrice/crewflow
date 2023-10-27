from django import forms
from .models import BlogPost
from .models import Employee


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'author']


class AddEmployee(forms.ModelForm):
    class Meta:
        model = Employee

        fields = ["first_name",
                  "last_name",
                  "address",
                  "phone",
                  "email",
                  "position",
                  "dateOfEmployment",
                  "postalCode"]
        labels = {'first_name': "First Name",
                  'last_name': "Last_Name",
                  'address': "Employee Home Address",
                  'phone': "Employee Phone Number",
                  'email': "Employee Email Address",
                  'position': "Position of Employee",
                  'dateOfEmployment': "Date of Employment",
                  'postalCode': "Employee Postal Code"}

