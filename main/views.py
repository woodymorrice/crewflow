from django.shortcuts import render

# view() generates requested pages based
# on the information here

def index(request):
    """Landing page for the main app
        of the project"""
    return render(request, 'main/index.html')
