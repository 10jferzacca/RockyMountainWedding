from django.shortcuts import render, redirect
from .models import Venue, Photographer
from .forms import VenueForm

# Venue Model Views

def venue_list(request):
    venues = Venue.objects.all()
    return render(request, 'wedding/venue_list.html', {'venues': venues})

def venue_detail(request, pk):
    venue = Venue.objects.get(id=pk)
    return render(request, 'wedding/venue_detail.html', {'venue': venue})

def venue_create(request):
    if request.method == 'POST':
        form = VenueForm(request.POST)
        if form.is_valid():
            venue = form.save()
            return redirect('venue_detail', pk=venue.pk)
    else:
        form = VenueForm()
    return render(request, 'wedding/venue_form.html', {'form': form})

def venue_edit(request, pk):
    venue = Venue.objects.get(pk=pk)
    if request.method == "POST":
        form = VenueForm(request.POST, instance=venue)
        if form.is_valid():
            venue = form.save()
            return redirect('venue_detail', pk=venue.pk)
    else:
        form = VenueForm(instance=venue)
    return render(request, 'wedding/venue_form.html', {'form': form})

def venue_delete(request, pk):
    Venue.objects.get(id=pk).delete()
    return redirect('venue_list')


#Photographer Model Views

def photographer_list(request):
    photographers = Photographer.objects.all()
    return render(request, 'wedding/photographer_list.html', {'photographers': photographers})

def photographer_detail(request, pk):
    photographer = Photographer.objects.get(id=pk)
    return render(request, 'wedding/photographer_detail.html', {'photographer': photographer})