from __future__ import unicode_literals

from django.db import models

class Listing(models.Model): 
	city = models.CharField(max_length=50, primary_key=True)
	lat = models.DecimalField(max_digits=8, decimal_places=5)
	long = models.DecimalField(max_digits=8, decimal_places=5)
	price = models.IntegerField()

	class Meta:
		db_table = 'listings'
