from django.urls import path
from . import views

# Define url patterns for the main app here
app_name = 'main'
urlpatterns = [
        # homepage
        path('', views.index, name='index'),
        path('announcement/<int:announcement_id>/', views.announcement_detail, name='announcement_detail'),
]
