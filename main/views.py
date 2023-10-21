from django.shortcuts import render
from .models import Announcement

def index(request):
    """Landing page for the main app
        of the project"""
    return render(request, 'main/index.html')

def announcement(request):
    """Landing page for the main app of the project"""
    sort_by = request.GET.get('sort_by', 'date_added')  # Default to sorting by date
    announcements = Announcement.objects.all().order_by(sort_by)
    #announcements = Announcement.objects.all()
    return render(request, 'main/announcement.html', {'announcements': announcements})


def announcement_detail(request, announcement_id):
    announcement = Announcement.objects.get(pk=announcement_id)
    return render(request, 'main/announcement_detail.html', {'announcement': announcement})