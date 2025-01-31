from django.contrib import admin
from .models import *


class NoticeAdmin(admin.ModelAdmin):
    list_display = ("id",)
    readonly_fields = ("id",)
    fields = ("id", "attachments")


admin.site.register(Notice, NoticeAdmin)


class NoticeENGAdmin(admin.ModelAdmin):
    list_display = ("id",)
    readonly_fields = ("id",)
    fields = ("id", "attachments")


admin.site.register(Notice_ENG, NoticeENGAdmin)
