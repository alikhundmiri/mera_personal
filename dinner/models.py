from django.db import models

# Create your models here.


class meal(models.Model):
	name = models.CharField(max_length=100, unique=True)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __str__(self):
		return self.name


	class Meta:
		ordering = ["-timestamp", "-updated"]
		verbose_name = "Meal Type"
		verbose_name_plural = "Meal Types"

class dishes(models.Model):
	name = models.CharField(max_length=100, unique=True)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	meal_type = models.ManyToManyField(meal, null=False, blank=False)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ["-timestamp", "-updated"]
		verbose_name = "Dish"
		verbose_name_plural = "Dishes"
