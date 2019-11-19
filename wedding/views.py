from django.shortcuts import render, redirect
from .models import Post, Venue, Photographer, Florist, Planner, Music, Catering, Bakery
from .forms import VenueForm

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'wedding/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'wedding/post_detail.html', {'post': post})

# Venue Model Views

def venue_list(request):
    venues = Venue.objects.all()
    return render(request, 'wedding/venue_list.html', {'venues': venues})

def venue_detail(request, pk):
    venue = Venue.objects.get(id=pk)
    return render(request, 'wedding/venue_detail.html', {'venue': venue})

#Photographer Model Views

def photographer_list(request):
    photographers = Photographer.objects.all()
    return render(request, 'wedding/photographer_list.html', {'photographers': photographers})

def photographer_detail(request, pk):
    photographer = Photographer.objects.get(id=pk)
    return render(request, 'wedding/photographer_detail.html', {'photographer': photographer})

# Florist Views

def florist_list(request):
    florists = Florist.objects.all()
    return render(request, 'wedding/florist_list.html', {'florist': florists})

def florist_detail(request, pk):
    florist = Florist.objects.get(id=pk)
    return render(request, 'wedding/florist_detail.html', {'florist': exapmle})

# Planner Views

def planner_list(request):
    planner = Planner.objects.all()
    return render(request, 'wedding/planner_list.html', {'planner': planner})

def planner_detail(request, pk):
    planner = Planners.objects.get(id=pk)
    return render(request, 'wedding/planner_detail.html', {'planner': exapmle})

# Music Views

def music_list(request):
    musics = Music.objects.all()
    return render(request, 'wedding/music_list.html', {'music': musics})

def music_detail(request, pk):
    music = Music.objects.get(id=pk)
    return render(request, 'wedding/music_detail.html', {'music': exapmle})

# Catering Views

def catering_list(request):
    caterings = Catering.objects.all()
    return render(request, 'wedding/catering_list.html', {'catering': caterings})

def catering_detail(request, pk):
    catering = Catering.objects.get(id=pk)
    return render(request, 'wedding/catering_detail.html', {'catering': exapmle})

# Baker Views

def bakery_list(request):
    bakerys = Bakery.objects.all()
    return render(request, 'wedding/bakery_list.html', {'bakery': bakerys})

def bakery_detail(request, pk):
    bakery = Bakery.objects.get(id=pk)
    return render(request, 'wedding/bakery_detail.html', {'bakery': exapmle})
