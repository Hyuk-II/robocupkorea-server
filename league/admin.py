from django.contrib import admin
from .models import *


class LeagueAdmin(admin.ModelAdmin):
    list_display = ("id",)
    fields = ("id", "attachments")


class LeagueENGAdmin(admin.ModelAdmin):
    list_display = ("id",)
    fields = ("id", "attachments")


admin.site.register(League, LeagueAdmin)
admin.site.register(League_ENG, LeagueENGAdmin)
