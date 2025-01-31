from django.contrib import admin
from .models import *


class NoticeAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    list_display = ("id",)
    readonly_fields = ("id",)
    fields = ("id", "attachments")


admin.site.register(Notice, NoticeAdmin)


class NoticeENGAdmin(admin.ModelAdmin):
    list_display = ("id",)
    readonly_fields = ("id",)
    fields = ("id", "attachments")


admin.site.register(Notice_ENG, NoticeENGAdmin)
=======
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
>>>>>>> 652834145c8626169bd95446f0ef30e63364fc39
