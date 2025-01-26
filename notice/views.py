from django.http import Http404, JsonResponse
from django.shortcuts import get_object_or_404, redirect
from .models import Attachment, Notice, Attachment_ENG, Notice_ENG
import os, mimetypes
from rest_framework.views import APIView


class Download(APIView):
    def get(self, request, pdf_name):
        lang = request.GET["lang"]
        if lang == "ko-KR":
            attach = get_object_or_404(Attachment, name=pdf_name)
        elif lang == "en-US":
            attach = get_object_or_404(Attachment_ENG, name=pdf_name)

        file_url = attach.document.url
        return redirect(file_url)


class GetNotices(APIView):
    def get(self, request):
        lang = request.GET["lang"]
        if lang == "ko-KR":
            notices = Notice.objects.all()
        elif lang == "en-US":
            notices = Notice_ENG.objects.all()

        if notices.exists():
            notices_list = [
                {
                    "id": notice.id,
                    "date": notice.date,
                    "author": "RCKA",
                    "title": notice.title,
                    "content": notice.content,
                    "attachmentsCount": notice.attachments.count(),
                }
                for notice in notices
            ]
            return JsonResponse({"notices": notices_list})
        else:
            raise Http404("leagues가 존재하지 않습니다.")


class GetNotice(APIView):
    def get(self, request, notice_id):
        lang = request.GET["lang"]
        if lang == "ko-KR":
            notice = get_object_or_404(Notice, pk=notice_id)
        elif lang == "en-US":
            notice = get_object_or_404(Notice_ENG, pk=notice_id)
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
            "author": "RCKA",
            "title": notice.title,
            "content": notice.content,
            "attachments": attachments,
        }

        return JsonResponse(response)
