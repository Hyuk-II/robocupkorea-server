from django.contrib import admin
from .models import *


class LeagueAdmin(admin.ModelAdmin):
    search_fields = ["id"]


class AttachAdmin(admin.ModelAdmin):
    exclude = ("name", "size")


admin.site.register(League, LeagueAdmin)
admin.site.register(Attachment, AttachAdmin)
