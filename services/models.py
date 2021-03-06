from django.db import models

class Service(models.Model):
	title = models.CharField(max_length=255)
	icon = models.ImageField(upload_to='services/')
	description = models.TextField()
	image = models.ImageField(upload_to='services/')
	slug = models.SlugField(max_length=255, blank=True)

	def __str__(self):
		return self.title

	class Meta:		
		verbose_name_plural = 'Servicios'

	def get_absolute_url(self):
		return '/servicios/%s/' % self.slug
