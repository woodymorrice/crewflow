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
        path('request_time_off/', views.request_time_off, name='request_time_off')

]
urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)