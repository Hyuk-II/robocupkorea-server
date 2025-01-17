from django.http import FileResponse, Http404, JsonResponse
from django.core.files.storage import FileSystemStorage
from django.shortcuts import get_object_or_404
from .models import Attachment, Notice
import os, mimetypes


def download(request, pdf_name):
    attach = get_object_or_404(Attachment, name=pdf_name)
    document = attach.document
    file_path = document.path
    fs = FileSystemStorage(file_path)
    response = FileResponse(fs.open(file_path, "rb"))
    response["Content-Disposition"] = (
        f"attachment; filename={os.path.basename(document.name)}"
    )
    return response


def get_notices(request):
    notices = Notice.objects.all()

    if notices.exists():
        notices_list = []
        for notice in notices:
            attachments = [
                {
                    "name": os.path.basename(attachment.document.name),
                    "href": attachment.document.url if attachment.document else None,
                    "type": mimetypes.guess_type(attachment.document.name)[0],
                    "size": attachment.document.size if attachment.document else None,
                }
                for attachment in notice.attachments.all()
            ]
            notices_list.append(
                {
                    "id": notice.id,
                    "date": notice.date,
                    "author": notice.author,
                    "title": notice.title,
                    "content": notice.content,
                    "attachments": attachments,
                }
            )
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
            "size": attachment.document.size if attachment.document else None,
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
