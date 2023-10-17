# Define url patterns for account management here
from django.urls import path, include

app_name = 'account'
urlpatterns = [
    # Uses default django authorization urls
    path('', include('django.contrib.auth.urls')),
]
