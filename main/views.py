from django.shortcuts import render
from .models import Announcement

def index(request):
    """Landing page for the main app of the project"""
    announcements = Announcement.objects.all()
    return render(request, 'main/index.html', {'announcements': announcements})


def announcement_detail(request, announcement_id):
    announcement = Announcement.objects.get(pk=announcement_id)
    return render(request, 'main/announcement_detail.html', {'announcement': announcement})