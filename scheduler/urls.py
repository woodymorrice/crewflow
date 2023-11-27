from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.urls import include, path
from main import views


from django.contrib import admin
from django.conf import settings


admin.autodiscover()

urlpatterns = [
    #path('scheduler/', include('scheduler.urls')),
    path('fullcalendar/', TemplateView.as_view(template_name="fullcalendar.html"), name='fullcalendar'),
    path('admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

