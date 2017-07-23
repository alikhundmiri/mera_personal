from django.db import models
from django.core.urlresolvers import reverse

EVENT_MODE = (
	(1, "Mahendi"),
	(2, "Wedding"),
	(3, "Reception"),
	)

class bride_list(models.Model):
	name = models.CharField(max_length=1200, blank=False, null=False)
	father_name = models.CharField(max_length=1200, blank=True, null=True)
	def __str__(self):
		return "%s, Daughter of %s" %(self.name, self.father_name)
	class Meta:
		verbose_name = "Bride"
		verbose_name_plural = "Brides"

class bridegroom_list(models.Model):
	name = models.CharField(max_length=1200, blank=False, null=False)
	father_name = models.CharField(max_length=1200, blank=True, null=True)
	def __str__(self):
		return "%s, Son of %s" %(self.name, self.father_name)
	class Meta:
		verbose_name = "Bridegroom"
		verbose_name_plural = "Bridegrooms"

class all_location(models.Model):
	hall_name = models.CharField(max_length=1200, blank=False, null=False)
	hall_location = models.TextField(max_length=12000, blank=True, null=True)
	
	def __str__(self):
		return self.hall_name
	class Meta:
		verbose_name = "Function Hall"
		verbose_name_plural = "Function Halls"

class events(models.Model):
	event_date = models.DateTimeField(auto_now=False, auto_now_add=False)
	event_type = models.IntegerField(choices=EVENT_MODE)
	bride_side = models.ManyToManyField("bride_list")
	bridegroom_side = models.ManyToManyField("bridegroom_list")
	event_location = models.ManyToManyField("all_location")
	event_similar = models.ManyToManyField("self", blank=True, null=True)
	def __str__(self):
		return "%s on %s" %(self.get_event_type_display(), self.event_date) 
	def get_absolute_url(self):
		return reverse("cereminder:detail", kwargs={"id" : self.id})

	class Meta:
		verbose_name = "Event"
		verbose_name_plural = "Events"
