from django.contrib import admin
from .models import Venue, Photographer
# Register your models here.


admin.site.register([Venue, Photographer])