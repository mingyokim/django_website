from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import CityForm

from airbnb.models import Listing

def show_heatmap(request):
	return render(request, 'airbnb/heatmap.html', {'allListings': Listing.objects.filter(city=CITY)})

def get_city(request):
	if request.method == 'POST':
		form = CityForm(request.POST)
		if form.is_valid():
			CITY = form.cleaned_data['city']
			print(CITY)
			#return HttpResponseRedirect('/airbnb/heatmap')
			form = CityForm()
			return render(request, 'airbnb/heatmap.html', {'allListings': Listing.objects.filter(city=CITY), 'form': form})
	else:
		form = CityForm()
		return render(request, 'airbnb/project.html', {'form': form})	

