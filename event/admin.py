from django.contrib import admin
from .models import Event, ETC


class EventAdmin(admin.ModelAdmin):
    search_fields = ["title"]


class ETCAdmin(admin.ModelAdmin):
    search_fields = ["title"]


admin.site.register(Event, EventAdmin)
admin.site.register(ETC, ETCAdmin)
