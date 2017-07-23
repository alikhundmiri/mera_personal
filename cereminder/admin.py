from django.contrib import admin
from .models import events, bride_list, bridegroom_list, all_location

class EventsAdmin(admin.ModelAdmin):
	list_display = ["event_date","id", "event_type"]
	list_filter = ["event_date", "event_type"]
	search_fields = ["event_date", "event_type"]
	filter_horizontal = ['bridegroom_side', "bride_side", "event_location","event_similar"]

	class Meta:
		model = events


class BrideAdmin(admin.ModelAdmin):
	list_display = ["name", "father_name"]
	list_filter = ["name", "father_name"]
	search_fields = ["name", "father_name"]

	class Meta:
		model = bride_list

class BrideGroomAdmin(admin.ModelAdmin):
	list_display = ["name", "father_name"]
	list_filter = ["name", "father_name"]
	search_fields = ["name", "father_name"]

	class Meta:
		model = bridegroom_list

class LocationAdmin(admin.ModelAdmin):
	list_display = ["hall_name", "hall_location"]
	list_filter = ["hall_name", "hall_location"]
	search_fields = ["hall_name", "hall_location"]

	class Meta:
		model = all_location


admin.site.register(events, EventsAdmin)
admin.site.register(bride_list, BrideAdmin)
admin.site.register(bridegroom_list, BrideGroomAdmin)
admin.site.register(all_location, LocationAdmin)
