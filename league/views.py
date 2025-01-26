from django.http import Http404, JsonResponse
from django.shortcuts import get_object_or_404, redirect
from .models import Attachment, League, Attachment_ENG, League_ENG
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


class GetAttachments(APIView):
    def get(self, request, league_id):
        lang = request.GET["lang"]
        if lang == "ko-KR":
            league = get_object_or_404(League, pk=league_id)
        elif lang == "en-US":
            league = get_object_or_404(League_ENG, pk=league_id)

        attachments = [
            {
                "name": os.path.basename(attachment.document.name),
                "href": attachment.document.url if attachment.document else None,
                "type": mimetypes.guess_type(attachment.document.name)[0],
                "size": attachment.size,
            }
            for attachment in league.attachments.all()
        ]
        return JsonResponse({"attachments": attachments})


class GetLeagues(APIView):
    def get(self, request):
        lang = request.GET["lang"]
        if lang == "ko-KR":
            leagues = League.objects.all()
        elif lang == "en-US":
            leagues = League_ENG.objects.all()

        if leagues.exists():
            leagues_list = []
            for league in leagues:
                leagues_list.append(
                    {
                        "id": league.id,
                        "date": league.date,
                        "author": "RCKA",
                        "title": league.title,
                        "content": league.content,
                        "attachments": league.attachments.count(),
                    }
                )
            return JsonResponse({"leagues": leagues_list})
        else:
            raise Http404("leagues가 존재하지 않습니다.")


class GetLeague(APIView):
    def get(self, reqeust, league_id):
        lang = reqeust.GET["lang"]
        if lang == "ko-KR":
            league = get_object_or_404(League, pk=league_id)
        elif lang == "en-US":
            league = get_object_or_404(League_ENG, pk=league_id)

        attachments = [
            {
                "name": os.path.basename(attachment.document.name),
                "href": attachment.document.url if attachment.document else None,
                "type": mimetypes.guess_type(attachment.document.name)[0],
                "size": attachment.size,
            }
            for attachment in league.attachments.all()
        ]
        response = {
            "id": league.id,
            "date": league.date,
            "author": "RCKA",
            "title": league.title,
            "content": league.content,
            "attachments": attachments,
        }

        return JsonResponse({"leagues": response})
