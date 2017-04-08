from django.contrib import admin
from .models import document_data

class dbModelAdmin(admin.ModelAdmin):
    list_display = ["time_of_record","cat_0","cat_1","cat_2","cat_3","cat_4","cat_5","cat_6","cat_7","cat_8","cat_9", "updated", "timestamp"]
    list_filter = ["cat_0", "time_of_record", "updated", "timestamp"]
    search_fields = ["time_of_record","cat_0","cat_1","cat_2","cat_3","cat_4","cat_5","cat_6","cat_7","cat_8","cat_9", "updated", "timestamp"]

    class Meta:
        model = document_data


admin.site.register(document_data, dbModelAdmin)

