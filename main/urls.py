from django.urls import path
from . import views

# Define url patterns for the main app here
app_name = 'main'
urlpatterns = [
        # homepage
        path('', views.index, name='index'),
        path('announcement/', views.announcement, name='announcement'),
        path('announcement/<int:announcement_id>/', views.announcement_detail, name='announcement_detail'),
        path('', views.addEmployee, name='addEmployee'),

        path('blog/blog_list/', views.blog_list, name='blog_list'),

        path('blog/create/', views.create_blog_post, name='create_blog_post'),
]