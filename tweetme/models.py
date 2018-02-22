from django.core.urlresolvers import reverse
from django.conf import settings
from django.db import models
from django.utils import timezone
TWEET_STATUS = (
	(0, "Scheduled"),
	(1, "Tweeted"),
	(2, "Error"),
	)

MEDIA_TYPE = (
	(0, "Nill"),
	(1, "Attached"),
	(2, "URL"),
	)


def upload_location(tweeting, filename):
    return "%s/%s/%s" %(tweeting.app_name, tweeting.id, filename)


class tweeting(models.Model):
	app_name = "Tweetme"
	tweet = models.TextField(max_length=140, blank=False, null=False)
	tweeton = models.DateTimeField(auto_now=False, auto_now_add=False, default=timezone.now())
	image_type = models.IntegerField(choices=MEDIA_TYPE, default=MEDIA_TYPE[0][0])
	image_url = models.TextField(max_length=1400, blank=True, null=True)
	image_upload = models.ImageField(
		upload_to=upload_location,
		null = True,
		blank = True,
		height_field = "height_field",
		width_field = "width_field",
	)
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)
	
	status = models.IntegerField(choices=TWEET_STATUS, default=TWEET_STATUS[0][0])	

	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)

	def __str__(self):
		return str(self.id)

	def get_absolute_url(self):
		return reverse("tweetme:detail", kwargs={"id" : self.id})

	class Meta:
		ordering = ["-timestamp", "-updated", '-tweeton']

