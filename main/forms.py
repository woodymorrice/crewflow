from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Announcement, BlogPost, ExpenseReport, TimeOffRequest, Comment, Availability
from account.models import Employee


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'photo']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['photo'].required = False


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
                  "role",
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
                  'role': "Role",
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
    details = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4, 'cols': 40})
    )
    class Meta:
        model = TimeOffRequest
        fields = ['start_date',
                  'end_date',
                  'reason',
                  'details',]
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'reason': forms.Select(choices=TimeOffRequest.REASON_CHOICES)
        }


class AvailabilityForm(forms.ModelForm):
    class Meta:
        model = Availability
        fields = ['m_start_time',
                  'm_end_time',
                  't_start_time',
                  't_end_time',
                  'w_start_time',
                  'w_end_time',
                  'th_start_time',
                  'th_end_time',
                  'f_start_time',
                  'f_end_time',
                  ]

        widgets = {
            'm_start_time': forms.TimeInput(attrs={'type': 'time'}),
            'm_end_time': forms.TimeInput(attrs={'type': 'time'}),
            't_start_time': forms.TimeInput(attrs={'type': 'time'}),
            't_end_time': forms.TimeInput(attrs={'type': 'time'}),
            'w_start_time': forms.TimeInput(attrs={'type': 'time'}),
            'w_end_time': forms.TimeInput(attrs={'type': 'time'}),
            'th_start_time': forms.TimeInput(attrs={'type': 'time'}),
            'th_end_time': forms.TimeInput(attrs={'type': 'time'}),
            'f_start_time': forms.TimeInput(attrs={'type': 'time'}),
            'f_end_time': forms.TimeInput(attrs={'type': 'time'}),
        }
