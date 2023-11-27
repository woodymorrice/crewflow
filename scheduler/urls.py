from django.views.generic import TemplateView
from django.conf.urls import include, url
from django.urls import path
from main import views


from django.contrib import admin
from django.conf import settings


admin.autodiscover()

urlpatterns = [
    # Index
    path('', views.index, name='index'),

    url(r'^$', TemplateView.as_view(template_name="homepage.html"),),
    url(r'^schedule/', include('schedule.urls')),
    url(r'^fullcalendar/', TemplateView.as_view(template_name="fullcalendar.html"), name='fullcalendar'),
    url(r'^admin/', admin.site.urls),

    # View Schedule
    path('view_schedule/', views.view_schedule, name='view_schedule'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
