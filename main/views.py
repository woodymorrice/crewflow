from django.shortcuts import render, get_object_or_404
from .models import Announcement

def index(request):
    """Landing page for the main app
        of the project"""
    return render(request, 'main/index.html')

def announcement(request):
    """Landing page for the main app of the project"""
    sort_by = request.GET.get('sort_by', '-date_added')  # Default to sorting by date
    search = request.GET.get('search', '')

    # Retrieve announcements based on sorting and search
    announcements = Announcement.objects.filter(title__icontains=search).order_by(sort_by)

    #announcements = Announcement.objects.all().order_by(sort_by)
    #announcements = Announcement.objects.all()
    return render(request, 'main/announcement.html', {'announcements': announcements})


def announcement_detail(request, announcement_id):
    announcement = get_object_or_404(Announcement, pk=announcement_id)

    # Mark the announcement as read
    announcement.read = True
    announcement.save()

    return render(request, 'main/announcement_detail.html', {'announcement': announcement})