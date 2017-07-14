from django.contrib import admin
from .models import dishes, meal

class DishesAdmin(admin.ModelAdmin):
	list_display = ["name", "timestamp", "updated"]
	list_filter = ["name", "timestamp", "updated"]
	search_fields = ["name", "timestamp", "updated"]
	filter_horizontal = ['meal_type']

	class Meta:
		model = dishes

class MealsAdmin(admin.ModelAdmin):
	list_display = ["name", "timestamp", "updated"]
	list_filter = ["name", "timestamp", "updated"]
	search_fields = ["name", "timestamp", "updated"]

	class Meta:
		model = meal

admin.site.register(dishes, DishesAdmin)
admin.site.register(meal, MealsAdmin)