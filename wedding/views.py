from django.shortcuts import render, redirect
from .models import Venue
from .forms import VenueForm

# Create your views here.
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