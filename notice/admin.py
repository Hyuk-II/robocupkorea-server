from django.contrib import admin
from .models import *


class NoticeAdmin(admin.ModelAdmin):
    search_fields = ["id"]


class AttachAdmin(admin.ModelAdmin):
    exclude = ("name", "size")


class NoticeENGAdmin(admin.ModelAdmin):
    search_fields = ["id"]


class AttachENGAdmin(admin.ModelAdmin):
    exclude = ("name", "size")


admin.site.register(Notice, NoticeAdmin)
admin.site.register(Attachment, AttachAdmin)
admin.site.register(Notice_ENG, NoticeENGAdmin)
admin.site.register(Attachment_ENG, AttachENGAdmin)
