from django.db import models
from django.conf import settings
# Create your models here.


PLATFORM_TYPE = (
	('Text', 'Text'),
	('Audio', 'Audio'),
	('Video', 'Video'),
	('Games', 'Games'),
	('Apps', 'Apps'),
	('Website', 'Website'),
	)

def platform_image_location(platform, filename):
	return "%s/%s/%s" %(platform.user, platform.id, filename)


class Type_of_Platform(models.Model):
	name					=			models.CharField(max_length=50, blank=False, null=False, default="")
	description				=			models.TextField(max_length=280, blank=True, null=True, default="")

	def __str__(self):
		return self.name

class platform(models.Model):
	# who is uploading this product
	user					=			models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
	image = models.ImageField(
		upload_to=platform_image_location,
		null = True,
		blank = True,
		height_field = "height_field",
		width_field = "width_field",
		)
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)

	# the product name
	platform_name			=			models.CharField(max_length=50, blank=False, null=False, default="")
	platform_description	=			models.TextField(max_length=280, blank=True, null=True, default="")
	platform_type			=			models.ManyToManyField(Type_of_Platform)

	# To Avoid spam content
	public_display			=			models.BooleanField(default=False)
	# If the product is uploaded by the maker, this needs to be done manually.
	# product_verified 		=			models.BooleanField(default=False)
	website					=			models.URLField(max_length=1000, blank=False, null=False, help_text="Your Landing page URL.")

	timestamp				=			models.DateTimeField(auto_now=False, auto_now_add=True)
	updated					=			models.DateTimeField(auto_now=True, auto_now_add=False)

	def __str__(self):
		return(self.platform_name)


class sources(models.Model):
	user					=			models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
	platform_reference		=			models.ForeignKey(platform, related_name='all_sources', blank=False, null=False, on_delete=models.CASCADE)	
	source_name				=			models.CharField(max_length=50, blank=False, null=False, default="")
	source_description		=			models.TextField(max_length=280, blank=True, null=True, default="")
	# To Avoid spam content
	public_display			=			models.BooleanField(default=False)
	website					=			models.URLField(max_length=1000, blank=False, null=False, help_text="Your Landing page URL.")
	
	timestamp				=			models.DateTimeField(auto_now=False, auto_now_add=True)
	updated					=			models.DateTimeField(auto_now=True, auto_now_add=False)

	def __str__(self):
		return(self.source_name)


# seperate class for urls bunch connected via Foreign key, to be displayed in detail view