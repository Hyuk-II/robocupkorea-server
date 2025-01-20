from django.contrib import admin
from .models import *


class AttachAdmin(admin.ModelAdmin):
    exclude = ("name", "size")


admin.site.register(Notice)
admin.site.register(Attachment, AttachAdmin)
