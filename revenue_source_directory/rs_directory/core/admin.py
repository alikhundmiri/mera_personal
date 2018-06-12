from django.contrib import admin

from .models import (Type_of_Platform, platform, sources)
# Register your models here.


class TypePlatformAdmin(admin.ModelAdmin):
	list_display = ["name", "description"]
	list_filter = ["name", "description"]
	search_fields = ["name", "description"]
	class Meta:
		model = Type_of_Platform

class PlatformAdmin(admin.ModelAdmin):
	list_display = ["platform_name", "user", "platform_description",  "updated", "public_display",]
	list_filter = ["platform_name","platform_description", "timestamp", "updated"]
	search_fields = ["user", "platform_name", "platform_description", "public_display", "updated"]
	filter_horizontal = ['platform_type']
	list_editable = ['public_display']

	class Meta:
		model = platform

class SourceAdmin(admin.ModelAdmin):
	list_display = ["platform_reference", "website", "source_description", "source_name", "public_display"]
	list_filter = ["platform_reference", "public_display", "website", "source_name", "source_description"]
	search_fields = ["platform_reference", "public_display", "website", "source_name", "source_description"]
	list_editable = ['public_display']
	class Meta:
		model = sources



admin.site.register(Type_of_Platform, TypePlatformAdmin)
admin.site.register(platform, PlatformAdmin)
admin.site.register(sources, SourceAdmin)



