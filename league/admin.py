from django.contrib import admin
from .models import *


class LeagueAdmin(admin.ModelAdmin):
    list_display = ("id",)
    fields = ("id", "attachments")


class LeagueENGAdmin(admin.ModelAdmin):
    list_display = ("id",)
    fields = ("id", "attachments")


class LeagueENGAdmin(admin.ModelAdmin):
    search_fields = ["id"]


class AttachENGAdmin(admin.ModelAdmin):
    exclude = ("name", "size")


admin.site.register(League, LeagueAdmin)
<<<<<<< HEAD
admin.site.register(League_ENG, LeagueENGAdmin)
=======
admin.site.register(Attachment, AttachAdmin)
admin.site.register(League_ENG, LeagueENGAdmin)
admin.site.register(Attachment_ENG, AttachENGAdmin)
>>>>>>> 652834145c8626169bd95446f0ef30e63364fc39
