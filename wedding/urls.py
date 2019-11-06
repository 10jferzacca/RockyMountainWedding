from django.urls import path
from . import views

urlpatterns = [
    path('', views.venue_list, name='venue_list'),
    path('venues/<int:pk>', views.venue_detail, name='venue_detail'),
    path('venue/new', views.venue_create, name='venue_create'),
]