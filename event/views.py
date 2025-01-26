from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Event


def get_events(request):
    events = Event.objects.all()
    events_list = [
        {
            "id": event.id,
            "title": event.title,
            "images": [event.image_top.url if event.image_top else None],
        }
        for event in events
    ]
    return JsonResponse({"events": events_list}, status=200)


def latest(request):
    latest_event = Event.objects.order_by("-start_date").first()
    if latest_event:
        result = {
            "id": latest_event.id,
            "title": latest_event.title,
            "dates": [latest_event.start_date, latest_event.end_date],
            "location": latest_event.location,
            "register": latest_event.register,
        }
        return JsonResponse(result, status=200)
    else:
        return JsonResponse({"error": "No events found"}, status=404)


def get_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    others = [
        {"title": etc.title, "description": etc.description}
        for etc in event.others.all()
    ]
    result = {
        "id": event.id,
        "title": event.title,
        "dates": [event.start_date, event.end_date],
        "location": event.location,
        "map": event.map,
        "register": event.register,
        "images": [
            event.image_top.url if event.image_top else None,
            event.image_bottom.url if event.image_bottom else None,
        ],
        "others": others,
        "leagues": event.leagues,
    }
    return JsonResponse(result, status=200)
