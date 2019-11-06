from django.urls import path
from . import views

urlpatterns = [
    path('', views.venue_list, name='venue_list'),
    path('venues/<int:pk>', views.venue_detail, name='venue_detail'),
    path('venue/new', views.venue_create, name='venue_create'),
    path('venue/<int:pk>/edit', views.venue_edit, name='venue_edit'),
    path('venue/<int:pk>/delete', views.venue_delete, name='venue_delete'),
]