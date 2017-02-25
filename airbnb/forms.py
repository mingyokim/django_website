from django import forms

CITY_CHOICES = [('New York City', 'New York City'), ('Paris', 'Paris'), ('Amsterdam', 'Amsterdam')]

class CityForm(forms.Form):
	city = forms.ChoiceField(
			required=True,
			widget=forms.RadioSelect,
			choices=CITY_CHOICES,
	)

