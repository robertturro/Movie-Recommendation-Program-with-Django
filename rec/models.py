from django.db import models

class Recommendation(models.Model):

	movie_input = models.CharField(max_length=100)
	release_year = models.FloatField(default=0)
	result = models.CharField(max_length=100)
	overview = models.CharField(max_length=3000, default='None')

	def __str__(self):
		return self.result

