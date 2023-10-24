from django.contrib import admin

# Here we define what models can be
# managed by the administrator

# Import the model
from .models import Announcement
from .models import Person

# and register it using this function
admin.site.register(Announcement)
admin.site.register(Person)
