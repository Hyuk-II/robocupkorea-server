from django.contrib import admin
from .models import Event, Event_ENG


class EventAdmin(admin.ModelAdmin):
    search_fields = ["title"]


class EventENGAdmin(admin.ModelAdmin):
    search_fields = ["title"]


admin.site.register(Event, EventAdmin)
admin.site.register(Event_ENG, EventENGAdmin)
