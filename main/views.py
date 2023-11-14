from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Announcement, BlogPost, AnnouncementReadStatus, ExpenseReport
from account.models import Employee
from .forms import BlogPostForm, AddEmployeeForm, AnnouncementForm, ExpenseReportForm
from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime, date
from django.contrib import messages


def is_admin(user):
    """Defined user permission"""
    return user.is_authenticated and user.is_staff

@login_required(login_url='account/login/')
def index(request):
    """Landing page for the main app
        of the project"""
    return render(request, 'main/index.html')


@login_required(login_url='account/login/')
def announcement(request):
    """Announcement overview"""
    sort_by = request.GET.get('sort_by', '-date_added')  # Default to sorting by date
    search = request.GET.get('search', '')

    # Retrieve announcements based on sorting and search
    announcements = Announcement.objects.filter(title__icontains=search).order_by(sort_by)
    for announcement in announcements:
        announcement.read = AnnouncementReadStatus.objects.filter(user=request.user, announcement=announcement).exists()

    return render(request, 'main/announcement.html', {'announcements': announcements})


@login_required(login_url='account/login/')
def announcement_detail(request, announcement_id):
    announcement = get_object_or_404(Announcement, pk=announcement_id)

    # Mark the announcement as read
    AnnouncementReadStatus.objects.get_or_create(user=request.user, announcement=announcement, defaults={'read': True})

    return render(request, 'main/announcement_detail.html', {'announcement': announcement})

@login_required(login_url='account/login/')
@user_passes_test(is_admin, login_url='main:announcement')
def add_announcement(request):
    if request.method == 'POST':
        form = AnnouncementForm(request.POST)
        if request.user.is_authenticated:
            announcement = form.save(commit=False)
            announcement.author = request.user
            announcement.save()
            return redirect('main:announcement_detail', announcement.id)  # Redirect to the announcement detail page
    else:
        form = AnnouncementForm()

    return render(request, 'main/add_announcement.html', {'form': form})

@login_required(login_url='account/login/')
def delete_announcement(request, announcement_id):
    # Get the announcement object to be deleted
    announcement = get_object_or_404(Announcement, pk=announcement_id)

    # Check if the user is an admin (staff member)
    if not request.user.is_staff:
        # Redirect the user to the announcement detail page
        messages.error(request, "You do not have permission to delete this announcement.")
        return redirect('main:announcement_detail', announcement_id)

    if request.method == 'POST':
        # Delete the announcement
        announcement.delete()
        messages.success(request, "Announcement deleted successfully.")
        return redirect('main:announcement')

    return render(request, 'main/delete_announcement.html', {'announcement': announcement})


@login_required(login_url='account/login/')
def add_employee(request):
    if request.method == "POST":
        form = AddEmployeeForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return redirect('main:view_employees')
    else:
        form = AddEmployeeForm()
    return render(request, 'main/add_employee.html', {'form': form})


@login_required(login_url='account/login/')
def view_employees(request):
    employee_list = Employee.objects.all()
    return render(request, 'main/view_employees.html', {'employee_list': employee_list})


@login_required(login_url='account/login/')
def blog_list(request):
    blog_posts = BlogPost.objects.all()
    return render(request, './main/blog_list.html', {'blog_posts': blog_posts})


@login_required(login_url='account/login/')
def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            new_blog_post = form.save(commit=False)
            # Set the author to the currently logged-in user's username
            new_blog_post.author = request.user
            # Save the blog post with the author
            new_blog_post.save()
    else:
        form = BlogPostForm()

    return render(request, './main/addBlog.html', {'form': form})


@login_required(login_url='account/login/')
def employee_payroll(request):
    """
    page for view employee profile
    """
    employees = Employee.objects.all()

    total_payroll_expenses = sum(employee.salary for employee in employees)

    current_date = date.today()
    payroll_start_date = current_date.replace(day=1)

    if current_date.day <= 15:
        payroll_end_date = current_date
    else:
        next_month = current_date.replace(day=15)
        payroll_end_date = (next_month.replace(month=next_month.month + 1) if next_month.month < 12
                            else next_month.replace(year=next_month.year + 1, month=1))

    payroll_period = f"{payroll_start_date.strftime('%B')} {payroll_start_date.day}, {payroll_start_date.year} " \
                     f"- {payroll_end_date.strftime('%B')} {payroll_end_date.day}, {payroll_end_date.year}"

    context = {
        'total_payroll_expenses': total_payroll_expenses,
        'number_of_employees': len(employees),
        'payroll_period': payroll_period,
        'payroll_status': 'Pending Manager Approval',
        'user_is_manager': True,
    }

    return render(request, 'main/payroll.html', context)



#expense report
@login_required(login_url='account/login/')
def expense_reports(request):
    if request.user.is_staff:
        reports = ExpenseReport.objects.all()
    else:
        reports = ExpenseReport.objects.filter(requester=request.user)
    return render(request, 'main/expense_reports.html', {'reports': reports})

@login_required(login_url='account/login/')
def add_report(request):
    if request.method == 'POST':
        form = ExpenseReportForm(request.POST, request.FILES)
        if form.is_valid():
            report = form.save(commit=False)
            report.requester = request.user
            report.save()
            return redirect('main:expense_reports')
    else:
        form = ExpenseReportForm()
    return render(request, 'main/add_report.html', {'form': form})

@login_required(login_url='account/login/')
def report_detail(request, report_id):
    report = get_object_or_404(ExpenseReport, pk=report_id)
    if request.method == 'POST' and  request.user.is_staff:
        report.status = request.POST.get('status')
        report.save()
    return render(request, 'main/report_detail.html', {'report': report})
