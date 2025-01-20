from django.http import FileResponse, Http404, JsonResponse
from django.core.files.storage import FileSystemStorage
from django.shortcuts import get_object_or_404
from .models import Attachment, League
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


def get_attachments(request, league_id):
    league = get_object_or_404(League, pk=league_id)
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


def get_leagues(request):
    leagues = League.objects.all()

    if leagues.exists():
        leagues_list = []
        for league in leagues:
            leagues_list.append(
                {
                    "id": league.id,
                    "date": league.date,
                    "author": league.author,
                    "title": league.title,
                    "content": league.content,
                    "attachments": league.attachments.count(),
                }
            )
        return JsonResponse({"leagues": leagues_list})
    else:
        raise Http404("leagues가 존재하지 않습니다.")


def get_league(reqeust, league_id):
    league = get_object_or_404(League, pk=league_id)
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
        "author": league.author,
        "title": league.title,
        "content": league.content,
        "attachments": attachments,
    }
    return JsonResponse({"leagues": response})
