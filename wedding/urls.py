from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('posts/<int:pk>', views.post_detail, name='post_detail'),

    path('venues/', views.venue_list, name='venue_list'),
    path('venues/<int:pk>', views.venue_detail, name='venue_detail'),

    #Photographer 
    path('photographers/', views.photographer_list, name='photographer_list'),
    path('photographers/<int:pk>', views.photographer_detail, name='photographer_detail'),

    #Florist
    path('florists/', views.florist_list, name='florist_list'),
    path('florists/<int:pk>', views.florist_detail, name='florist_detail'),

    #Planners
    path('planners/', views.planner_list, name='planner_list'),
    path('planners/<int:pk>', views.planner_detail, name='planner_detail'),

    #Music
    path('musics/', views.music_list, name='music_list'),
    path('musics/<int:pk>', views.music_detail, name='music_detail'),

    #Catering 
    path('caterings/', views.catering_list, name='catering_list'),
    path('caterings/<int:pk>', views.catering_detail, name='catering_detail'),

    #Bakery
    path('bakerys/', views.bakery_list, name='bakery_list'),
    path('bakerys/<int:pk>', views.bakery_detail, name='bakery_detail'),
    ]