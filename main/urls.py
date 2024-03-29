from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from emp_man_sys import settings
from . import views

from django.conf.urls.static import static

# Define url patterns for the main app here
app_name = 'main'
urlpatterns = [
        # Index
        path('', views.index, name='index'),

        # Announcements
        path('announcement/', views.announcement, name='announcement'),
        path('announcement/<int:announcement_id>/', views.announcement_detail, name='announcement_detail'),
        path('add_announcement/', views.add_announcement, name='add_announcement'),
        path('delete_announcement/<int:announcement_id>/', views.delete_announcement, name='delete_announcement'),

        # Blogs

        path('blog/blog_list/', views.blog_list, name='blog_list'),
        path('blog/create/', views.create_blog_post, name='create_blog_post'),
        path('blog/<int:post_id>/', views.view_blog_details, name='view_blog_details'),
        path("blog/comment/<int:commentID>/", views.editCommentView, name="editCommentView"),
        path("blog/deletecomment/<int:commentID>", views.delete_comment, name="deleteComment"),
        path('blog/edit_blog_post/<int:post_id>/', views.edit_blog_post, name='edit_blog_post'),
        path("blog/deleteBlog/<int:post_id>", views.delete_blog, name="delete_blog"),


        # Payroll
        path('payroll/', views.employee_payroll, name='payroll'),
        path('approve_payroll/', views.approve_payroll, name='approve_payroll'),
        path('edit_employee_salary/<int:employee_id>/', views.edit_employee_salary, name='edit_employee_salary'),
        # Manager pages #

        # Add Employees
        path('add_employee/', views.add_employee, name='add_employee'),
        path('view_employees/', views.view_employees, name='view_employees'),
        path('edit_employee/<int:employee_id>/', views.edit_employee, name='edit_employee'),

        # expense report
        path('report_detail/<int:report_id>/', views.report_detail, name='report_detail'),
        path('expense_reports/', views.expense_reports, name='expense_reports'),
        path('add_report/', views.add_report, name='add_report'),
        path('delete_report/<int:report_id>/', views.delete_report, name='delete_report'),

        # Time Off Request
        path('request_time_off/', views.request_time_off, name='request_time_off'),
        path('delete_request/<int:request_id>/', views.delete_request, name="delete_request"),
        path('cancel_request/<int:request_id>/', views.cancel_request, name="cancel_request"),

        # delete notification
        path('delete_notification/<int:notification_id>/', views.delete_notification, name='delete_notification'),

        # Check requests
        path('check_time_off_requests/', views.check_time_off_requests, name='check_time_off_requests'),
        path('approve_request/<int:request_id>/', views.approve_request, name='approve_request'),
        path('decline_request/<int:request_id>/', views.decline_request, name='decline_request'),

        # Schedule
        path('schedule/', views.schedule_landing, name='schedule_landing'),
        path('edit_schedule/', views.edit_schedule, name='edit_schedule'),
        path('schedule/add_availability/', views.add_availability, name="add_availability"),
        path('schedule/availability/', views.view_availability, name="view_availability"),
        path('schedule/availabilities/', views.view_availabilities, name="view_availabilities"),
        path('schedule/edit_availability/<int:avail_id>', views.edit_availability, name="edit_availability"),

        # Profile
        path('view_profile/', views.view_profile, name='view_profile'),

]
urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
