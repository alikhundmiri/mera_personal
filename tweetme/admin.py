from django.contrib import admin
from .models import tweeting


class TweetAdmin(admin.ModelAdmin):
	list_display = ["tweet", "tweeton", "status", 'image_type', "timestamp", "updated"]
	list_filter = ["tweet", "tweeton", "status", 'image_type', "timestamp", "updated"]
	search_fields = ["tweet", "tweeton", "status", 'image_type', "timestamp", "updated"]

	class Meta:
		model = tweeting

admin.site.register(tweeting, TweetAdmin)
