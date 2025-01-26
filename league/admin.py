from django.contrib import admin
from .models import *


class LeagueAdmin(admin.ModelAdmin):
    search_fields = ["id"]


class AttachAdmin(admin.ModelAdmin):
    exclude = ("name", "size")


class LeagueENGAdmin(admin.ModelAdmin):
    search_fields = ["id"]


class AttachENGAdmin(admin.ModelAdmin):
    exclude = ("name", "size")


admin.site.register(League, LeagueAdmin)
admin.site.register(Attachment, AttachAdmin)
admin.site.register(League_ENG, LeagueENGAdmin)
admin.site.register(Attachment_ENG, AttachENGAdmin)
