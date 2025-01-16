from django.http import FileResponse, Http404, JsonResponse
from django.core.files.storage import FileSystemStorage
from django.shortcuts import get_object_or_404
from .models import Attachment, League
import os


def download(request, pdf_name):
    attach = get_object_or_404(Attachment, name=pdf_name)
    if attach:
        document = attach.document
        file_path = document.path
        fs = FileSystemStorage(file_path)
        response = FileResponse(fs.open(file_path, "rb"))
        response["Content-Disposition"] = (
            f"attachment; filename={os.path.basename(document.name)}"
        )
        return response
    else:
        return Http404


def get_attachments(request, league_id):
    league = get_object_or_404(League, pk=league_id)
    attachments = Attachment.objects.filter(id__in=league.attachments)
    attach_list = [
        {
            "name": [attachment.name if attachment.document else None],
            "href": [attachment.document.url if attachment.document else None],
            "type": [attachment.type if attachment.document else None],
            "size": [attachment.document.size if attachment.document else None],
        }
        for attachment in attachments
    ]
    return JsonResponse({"attachments": attach_list})


def get_leagues(request):
    leagues = League.objects.all()
    if leagues:
        leagues_list = []
        for league in leagues:
            attachments = Attachment.objects.filter(id__in=league.attachments)
            attach_list = [
                {
                    "name": [attachment.name if attachment.document else None],
                    "href": [attachment.document.url if attachment.document else None],
                    "type": [attachment.type if attachment.document else None],
                    "size": [attachment.document.size if attachment.document else None],
                }
                for attachment in attachments
            ]

            leagues_list.append(
                {
                    "id": league.id,
                    "date": league.date,
                    "author": league.author,
                    "title": league.title,
                    "content": league.content,
                    "attachments": attach_list,
                }
            )
        return JsonResponse({"leagues": leagues_list})
    else:
        return Http404


def get_league(reqeust, league_id):
    league = get_object_or_404(League, pk=league_id)
    attachments = Attachment.objects.filter(id__in=league.attachments)
    attach_list = [
        {
            "name": [attachment.name if attachment.document else None],
            "href": [attachment.document.url if attachment.document else None],
            "type": [attachment.type if attachment.document else None],
            "size": [attachment.document.size if attachment.document else None],
        }
        for attachment in attachments
    ]
    response = {
        "id": league.id,
        "date": league.date,
        "author": league.author,
        "title": league.title,
        "content": league.content,
        "attachments": attach_list,
    }
    return JsonResponse({"leagues": response})
