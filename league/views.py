from django.http import Http404, JsonResponse
from django.shortcuts import get_object_or_404, redirect
from .models import League, League_ENG
import os, mimetypes
from rest_framework.views import APIView


# class Download(APIView):
#     def get(self, request, pdf_name):
#         lang = request.GET["lang"]
#         if lang == "ko-KR":
#             attach = get_object_or_404(Attachment, name=pdf_name)
#         elif lang == "en-US":
#             attach = get_object_or_404(Attachment_ENG, name=pdf_name)

#         file_url = attach.document.url
#         return redirect(file_url)


class GetAttachments(APIView):
    def get(self, request, league_id):
        lang = request.GET["lang"]
        if lang == "ko-KR":
            league = get_object_or_404(League, pk=league_id)
        elif lang == "en-US":
            league = get_object_or_404(League_ENG, pk=league_id)

        return JsonResponse({"attachments": league.attachments})


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
                        "author": "RCKA",
                        "attachments": len(league.attachments),
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

        response = {
            "id": league.id,
            "author": "RCKA",
            "attachments": league.attachments,
        }

        return JsonResponse({"leagues": response})
