from django.db import models
from django.conf import settings


def advertisment_image_location(platform, filename):
	return "%s/%s/%s/%s" %("advertisment", platform.user, platform.id, filename)

class ads(models.Model):
	# who is uploading this product
	user					=			models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
	image 					= 			models.ImageField(
											upload_to=advertisment_image_location,
											null = True,
											blank = True,
											height_field = "height_field",
											width_field = "width_field",
										)
	height_field			=			models.IntegerField(default=0)
	width_field				=			models.IntegerField(default=0)

	# the product name
	client_name				=			models.CharField(max_length=50, blank=False, null=False, default="")
	client_description		=			models.TextField(max_length=280, blank=True, null=True, default="")

	# To Avoid spam content
	public_display			=			models.BooleanField(default=False)
	# If the product is uploaded by the maker, this needs to be done manually.
	# product_verified 		=			models.BooleanField(default=False)
	website					=			models.URLField(max_length=1000, blank=False, null=False, help_text="Your Landing page URL.")
	click_count				=			models.IntegerField(default=0)
	advert_time 			=			models.DateTimeField()

	timestamp				=			models.DateTimeField(auto_now=False, auto_now_add=True)
	updated					=			models.DateTimeField(auto_now=True, auto_now_add=False)

	def __str__(self):
		return(self.client_name)
