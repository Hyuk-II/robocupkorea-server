from django.http import FileResponse, Http404, JsonResponse
from django.shortcuts import get_object_or_404, redirect
from .models import Attachment, Notice
import os, mimetypes


def download(request, pdf_name):
    attach = get_object_or_404(Attachment, name=pdf_name)
    file_url = attach.document.url
    return redirect(file_url)


def get_notices(request):
    notices = Notice.objects.all()
    if notices.exists():
        notices_list = [
            {
                "id": notice.id,
                "date": notice.date,
                "author": notice.author,
                "title": notice.title,
                "content": notice.content,
                "attachmentsCount": notice.attachments.count(),
            }
            for notice in notices
        ]
        return JsonResponse({"notices": notices_list})
    else:
        raise Http404("leagues가 존재하지 않습니다.")


def get_notice(reqeust, notice_id):
    notice = get_object_or_404(Notice, pk=notice_id)
    attachments = [
        {
            "name": os.path.basename(attachment.document.name),
            "href": attachment.document.url if attachment.document else None,
            "type": mimetypes.guess_type(attachment.document.name)[0],
            "size": attachment.size,
        }
        for attachment in notice.attachments.all()
    ]
    response = {
        "id": notice.id,
        "date": notice.date,
        "author": notice.author,
        "title": notice.title,
        "content": notice.content,
        "attachments": attachments,
    }
    return JsonResponse(response)
