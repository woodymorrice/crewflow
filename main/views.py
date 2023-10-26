from django.shortcuts import render, get_object_or_404
from .models import Announcement
from .forms import BlogPostForm
from .models import BlogPost
from django.shortcuts import render, redirect

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

    return render(request, 'main/announcement.html', {'announcements': announcements})


def announcement_detail(request, announcement_id):
    announcement = get_object_or_404(Announcement, pk=announcement_id)

    # Mark the announcement as read
    announcement.read = True
    announcement.save()

    return render(request, 'main/announcement_detail.html', {'announcement': announcement})

def addEmployee(request):
    return render(request, 'main/addEmployee.html')

def blog_list(request):
    blog_posts = BlogPost.objects.all()
    return render(request, './main/blog_list.html', {'blog_posts': blog_posts})


def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)  # Use the form to handle data submission
        if form.is_valid():
            form.save()  # Save the new blog post to the database
            return redirect('blog_list')  # Redirect to the list of blog posts
    else:
        form = BlogPostForm()  # Create an empty form for a GET request

    return render(request, './main/addBlog.html', {'form': form})
