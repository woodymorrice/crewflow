from django.urls import path
from . import views

urlpatterns = [
    path('api/blog/list/', views.getData),
    path('api/blog/add/', views.addPost),
    path('api/blog/delete-data/<int:id>/', views.deleteData, name='delete-data'),
]