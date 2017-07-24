from django.contrib import admin
from .models import mywork, hosted_projects
# Register your models here.
class FirstModelAdmin(admin.ModelAdmin):
    list_display = ["title","type_work","role","purpose", "updated", "timestamp"]
    list_filter = ["updated", "timestamp"]
    search_fields = ["title", "detail"]
    class Meta:
        model = mywork

class HostedModelAdmin(admin.ModelAdmin):
    list_display = ["title","type_work","role","purpose", "updated", "timestamp"]
    list_filter = ["updated", "timestamp"]
    search_fields = ["title", "detail"]
    class Meta:
        model = hosted_projects

admin.site.register(mywork,FirstModelAdmin)
admin.site.register(hosted_projects,HostedModelAdmin)

