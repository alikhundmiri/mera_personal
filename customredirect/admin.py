from django.contrib import admin
from .models import redirect_elements

class RedirectAdmin(admin.ModelAdmin):
	list_display = ["title", "redirect_url", "count", "timestamp", "updated"]
	list_filter = ["title", "redirect_url", "count", "timestamp", "updated"]
	search_fields = ["title", "redirect_url", "count", "timestamp", "updated"]

	class Meta:
		model = redirect_elements

admin.site.register(redirect_elements, RedirectAdmin)
