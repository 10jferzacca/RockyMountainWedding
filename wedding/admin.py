from django.contrib import admin
from .models import Post, Venue, Photographer, Florist, Planner, Music, Catering, Bakery
# Register your models here.


admin.site.register([Post, Venue, Photographer, Florist, Planner, Music, Catering, Bakery])