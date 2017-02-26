from django import forms
from .models import Listing

CITY_CHOICES = [('New York City', 'New York City'), ('Paris', 'Paris'), ('Amsterdam', 'Amsterdam')]

class CityForm(forms.Form):
	city = forms.ChoiceField(
			required=True,
			widget=forms.RadioSelect,
			choices=[(c['city'], c['city']) for c in Listing.objects.values('city').distinct()], 
	)

