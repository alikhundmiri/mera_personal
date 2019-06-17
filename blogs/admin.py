from django.contrib import admin
from .models import Post, taggers

class BlogAdmin(admin.ModelAdmin):
	list_display = ["title", "timestamp", "updated"]
	list_filter = ["title", "timestamp", "updated"]
	search_fields = ["title", "timestamp", "updated", "detail", "user"]
	filter_horizontal = ['tags']

	class Meta:
		model = Post

admin.site.register(Post, BlogAdmin)

class TagAdmin(admin.ModelAdmin):
	list_display = ["tag_name","description"]
	list_filter = ["tag_name","description"]
	search_fields = ["tag_name","description"]

	class Meta:
		model = taggers

admin.site.register(taggers, TagAdmin)
