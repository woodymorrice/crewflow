import os

from django.contrib.auth.decorators import login_required, user_passes_test
from django.views import View

from .models import Announcement, BlogPost, AnnouncementReadStatus, ExpenseReport, TimeOffRequest, Comment, Notification
from account.models import Employee
from .forms import BlogPostForm, AddEmployeeForm, AnnouncementForm, ExpenseReportForm, TimeOffRequestForm, ChangeEmployeeForm, BlogCommentForm
from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime, date
from django.contrib import messages
from django.conf import settings
from django.http import HttpResponseRedirect


def can_anno(user):
    """Defined user permission"""
    return user.is_staff or user.can_announce or user.is_manager()

@login_required(login_url='account/login/')
def index(request):
    """Landing page for the main app
        of the project"""
    notifications = Notification.objects.filter(user=request.user)  # Fetch unread notifications
    return render(request, 'main/index.html', {'notifications': notifications})

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
@user_passes_test(can_anno, login_url='main:announcement')
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

    if request.method == 'POST':
        # Delete the announcement
        announcement.delete()
        messages.success(request, "Announcement deleted successfully.")
        return redirect('main:announcement')

    return render(request, 'main/announcement.html', {'announcement': announcement})


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
    query = request.GET.get('search', '')
    employee_list = Employee.objects.filter(first_name__icontains=query)
    return render(request, 'main/view_employees.html', {'employee_list': employee_list})

@login_required(login_url='account/login/')
def edit_employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    if request.method == 'POST':
        form = ChangeEmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('main:view_employees')
    else:
        form = ChangeEmployeeForm(instance=employee)
    context = {'employee': employee, 'form': form}
    return render(request, 'main/edit_employee.html', context)


@login_required(login_url='account/login/')
def blog_list(request):
    blog_posts = BlogPost.objects.all()
    return render(request, './main/blog_list.html', {'blog_posts': blog_posts})


@login_required(login_url='account/login/')
def view_blog_details(request, post_id):
    blog_post = get_object_or_404(BlogPost, pk=post_id)
    if request.method == 'POST':
        form = BlogCommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.post = blog_post
            new_comment.to_reply = post_id
            new_comment.save()
    else:
        form = BlogCommentForm()
    comments = Comment.objects.filter(to_reply=post_id)
    return render(request, './main/view_blog_details.html',
                  {'blog_post': blog_post, 'form': form, 'comments': comments})


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


def editCommentView(request, commentID):
    comment = Comment.objects.get(id=commentID)
    if request.method == 'POST':
        comment.content = request.POST.get("editCommentView")
        comment.save()
        return redirect('main:view_blog_details', post_id=comment.to_reply)
    context = {
        'comment': comment,
    }
    return render(request, 'main/editComment.html', context)


def delete_comment(request, commentID):
    comment = Comment.objects.get(id=commentID)
    x = comment.to_reply
    Comment.objects.get(id=commentID).delete()
    return redirect('main:view_blog_details', post_id=x)


def edit_blog_post(request, post_id):
    blog = BlogPost.objects.get(id=post_id)
    if request.method == 'POST':
        blog.content = request.POST.get("edit_blog_post")
        blog.save()
        return redirect('main:blog_list')
    context = {
        'blog': blog,
    }
    return render(request, 'main/editBlog.html', context)


def delete_blog(request, post_id):
    blog = BlogPost.objects.get(id=post_id)
    BlogPost.objects.get(id=blog.id).delete()
    return redirect('main:blog_list')



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
        'employee_list': employees,
    }

    return render(request, 'main/payroll.html', context)



#expense report
@login_required(login_url='account/login/')
def expense_reports(request):
    if request.user.is_staff or request.user.is_manager():
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
    is_requester = report.requester == request.user

    if request.user.is_staff or is_requester or request.user.is_manager() :
        if request.method == 'POST' and (request.user.is_staff or request.user.is_manager()):
            new_status = request.POST.get('status')
            report.status = new_status
            report.save()

            # Create a notification for the requester
            if new_status == 'APPROVED':
                status_message = "approved"
            elif new_status == 'DECLINED':
                status_message = "declined"
            else:
                status_message = "updated"

            message = f"Your report number: {report_id}, has been {status_message}"
            Notification.objects.create(user=report.requester, message=message)

        return render(request, 'main/report_detail.html', {'report': report})
    else:
        reports = ExpenseReport.objects.filter(requester=request.user)
        return render(request, 'main/expense_reports.html', {'reports': reports})


@login_required(login_url='account/login/')
def delete_report(request, report_id):
    report = get_object_or_404(ExpenseReport, pk=report_id)

    # Check if the current user has permission to delete this report
    if request.user.is_staff or request.user == report.requester or request.user.is_manager():
        if request.method == 'POST':
            # Delete the associated photo file
            if report.photo:
                # Get the path to the photo file and delete it from the storage
                photo_path = os.path.join(settings.MEDIA_ROOT, str(report.photo))
                if os.path.exists(photo_path):
                    os.remove(photo_path)

            # Delete the expense report
            report.delete()
            return redirect('main:expense_reports')


@login_required(login_url='account/login/')
def request_time_off(request):
    if request.method == 'POST':
        form = TimeOffRequestForm(request.POST)
        if form.is_valid():
            time_off_request = form.save(commit=False)
            time_off_request.employee = request.user
            time_off_request.status = 'pending'
            time_off_request.save()
            messages.success(request,
                             'Your time off request has been submitted and is pending approval')
            return HttpResponseRedirect(request.path_info)
    else:
        form = TimeOffRequestForm()

    requests = TimeOffRequest.objects.filter(employee=request.user)

    context = {
        'form': form,
        'requests': requests,
    }
    return render(request, 'main/timeoff_request.html', context)

@login_required(login_url='account/login/')
def delete_notification(request, notification_id):
    notification = get_object_or_404(Notification, pk=notification_id)
    if notification.user == request.user:
        notification.delete()
    return redirect('main:index')

@login_required(login_url='account/login/')
def check_time_off_requests(request):
    requests = TimeOffRequest.objects.filter(status='pending')
    return render(request, 'main/check_requests.html', {'requests':requests})

@login_required(login_url='account/login/')
def approve_request(request, request_id):
    time_off_request = TimeOffRequest.objects.get(pk=request_id)
    time_off_request.status = 'approved'
    time_off_request.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

@login_required(login_url='account/login/')
def view_schedule(request):
    return render(request, 'scheduler/fullcanlendar.html', {'view_schedule': view_schedule})


@login_required(login_url='account/login/')
def decline_request(request, request_id):
    time_off_request = TimeOffRequest.objects.get(pk=request_id)
    time_off_request.status = 'denied'
    time_off_request.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

@login_required(login_url='account/login/')
def delete_request(request, request_id):
    time_off_request = get_object_or_404(TimeOffRequest, id=request_id)
    time_off_request.delete()
    return redirect('main:request_time_off')

@login_required(login_url='account/login/')
def cancel_request(request, request_id):
    time_off_request = get_object_or_404(TimeOffRequest, id=request_id, employee=request.user)
    if time_off_request.status == 'pending':
        time_off_request.status = 'canceled'
        time_off_request.save()
    return redirect('main:request_time_off')