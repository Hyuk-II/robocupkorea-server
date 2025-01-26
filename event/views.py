from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Event, Event_ENG
from rest_framework.views import APIView


class GetEvents(APIView):
    def get(self, request):
        lang = request.GET["lang"]

        if lang == "ko-KR":
            events = Event.objects.all()
        elif lang == "en-US":
            events = Event_ENG.objects.all()

        events_list = [
            {
                "id": event.id,
                "title": event.title,
                "images": [event.image_top.url if event.image_top else None],
            }
            for event in events
        ]
        return JsonResponse({"events": events_list}, status=200)


class Latest(APIView):
    def get(self, reqeust):
        lang = reqeust.GET["lang"]

        if lang == "ko-KR":
            latest_event = Event.objects.order_by("-start_date").first()
        elif lang == "en-US":
            latest_event = Event_ENG.objects.order_by("-start_date").first()

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


class GetEvent(APIView):
    def get(self, request, event_id):
        lang = request.GET["lang"]

        if lang == "ko-KR":
            event = get_object_or_404(Event, pk=event_id)
        elif lang == "en-US":
            event = get_object_or_404(Event_ENG, pk=event_id)

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
            "others": event.others,
            "leagues": event.leagues,
        }
        return JsonResponse(result, status=200)
