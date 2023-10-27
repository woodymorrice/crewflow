from django.shortcuts import render, get_object_or_404
from .models import Announcement
from .forms import BlogPostForm
from .models import BlogPost
from django.shortcuts import render, redirect
from datetime import datetime, date

def index(request):
    """Landing page for the main app
        of the project"""
    return render(request, 'main/index.html')

def announcement(request):
    """Landing page for the main app of the project"""
    sort_by = request.GET.get('sort_by', '-date_added')  # Default to sorting by date
    search = request.GET.get('search', '')

    # Retrieve announcements based on sorting and search
    announcements = Announcement.objects.filter(title__icontains=search).order_by(sort_by)

    return render(request, 'main/announcement.html', {'announcements': announcements})


def announcement_detail(request, announcement_id):
    announcement = get_object_or_404(Announcement, pk=announcement_id)

    # Mark the announcement as read
    announcement.read = True
    announcement.save()

    return render(request, 'main/announcement_detail.html', {'announcement': announcement})


def add_employee(request):
    if request.method == "POST":
        form = AddEmployee(request.POST)
        if form.is_valid():
            form.save()
        else:
            form = AddEmployee()
    return render(request, 'main/addEmployee.html', {'form': form})

def blog_list(request):
    blog_posts = BlogPost.objects.all()
    return render(request, './main/blog_list.html', {'blog_posts': blog_posts})


def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)  # Use the form to handle data submission
        if form.is_valid():
            form.save()  # Save the new blog post to the database
            return redirect('blog_list')  # Redirect to the list of blog posts
    else:
        form = BlogPostForm()  # Create an empty form for a GET request

    return render(request, './main/addBlog.html', {'form': form})


def employee_payroll(request):
    """
    page for view employee profile
    """
    employees = [
        {
            'name': 'Employee 1',
            'salary': 5000,
            'bonus': 2000,
            'deductions': 1000,
        },
        {
            'name': 'Employee 2',
            'salary': 6000,
            'bonus': 2500,
            'deductions': 1200,
        },
        # Add more employees as needed
    ]

    # Calculate total payroll expenses
    total_payroll_expenses = sum(employee['salary'] + employee['bonus'] for employee in employees)

    # Calculate total deductions
    total_deductions = sum(employee['deductions'] for employee in employees)

    # Calculate total net payments
    total_net_payments = total_payroll_expenses - total_deductions

    # Calculate the average salary
    total_salaries = sum(employee['salary'] for employee in employees)
    average_salary = total_salaries / len(employees)

    current_date = date.today()

    # Calculate the start date (1st day of the current month)
    payroll_start_date = current_date.replace(day=1)

    # Calculate the end date (15th day of the current month)
    if current_date.day <= 15:
        payroll_end_date = current_date
    else:
        # If today is past the 15th, set the end date to the 15th of the next month
        next_month = current_date.replace(day=15)  # 15th of the current month
        payroll_end_date = (next_month.replace(month=next_month.month + 1) if next_month.month < 12
                            else next_month.replace(year=next_month.year + 1, month=1))

    # Format the dates as strings
    payroll_period = f"{payroll_start_date.strftime('%B')} {payroll_start_date.day}, {payroll_start_date.year} " \
                     f"- {payroll_end_date.strftime('%B')} {payroll_end_date.day}, {payroll_end_date.year}"

    context = {
        'total_payroll_expenses': total_payroll_expenses,
        'total_deductions': total_deductions,
        'total_net_payments': total_net_payments,
        'average_salary': average_salary,
        'number_of_employees': len(employees),
        'total_bonus_payments': sum(employee['bonus'] for employee in employees),
        'payroll_period': payroll_period,
        'payroll_status': 'Pending Manager Approval',
        'user_is_manager': True,
    }

    return render(request, 'main/payroll.html', context)
