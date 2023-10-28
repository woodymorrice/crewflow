from django.urls import path
from . import views

# Define url patterns for the main app here
app_name = 'main'
urlpatterns = [
        # Index
        path('', views.index, name='index'),

        # Announcements
        path('announcement/', views.announcement, name='announcement'),
        path('announcement/<int:announcement_id>/', views.announcement_detail, name='announcement_detail'),
        path('add_announcement/', views.add_announcement, name='add_announcement'),

        # Blogs
        path('blog/blog_list/', views.blog_list, name='blog_list'),
        path('blog/create/', views.create_blog_post, name='create_blog_post'),

        # Payroll
        path('payroll/', views.employee_payroll, name='payroll'),

        # Manager pages #

        # Add Employees
        path('addEmployee/', views.add_employee, name='addEmployee'),
        path('view_employees', views.view_employees, name='viewEmployees'),

]
