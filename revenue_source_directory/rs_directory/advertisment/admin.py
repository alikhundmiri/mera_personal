from django.contrib import admin
from .models import ads


class AdsAdmin(admin.ModelAdmin):
	list_display = ["client_name", "user", "client_description",  "updated", "public_display", 'click_count', 'advert_time']
	list_filter = ["client_name","client_description", "timestamp", "updated", 'click_count', 'advert_time']
	search_fields = ["user", "client_name", "client_description", "public_display", "updated", 'click_count', 'advert_time']
	list_editable = ['public_display']

	class Meta:
		model = ads

admin.site.register(ads, AdsAdmin)
