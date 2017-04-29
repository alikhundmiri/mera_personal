from django.contrib import admin
from .models import mywork
# Register your models here.
class FirstModelAdmin(admin.ModelAdmin):
    list_display = ["title","type_work","role","purpose", "updated", "timestamp"]
    list_filter = ["updated", "timestamp"]
    search_fields = ["title", "detail"]
    class Meta:
        model = mywork

admin.site.register(mywork,FirstModelAdmin)
