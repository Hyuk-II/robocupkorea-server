from django.http import JsonResponse, response
from .models import Event

def events(request):
    events = Event.objects.all()
    id_list = []
    for event in events:
        id_list.append(event.id)
    return JsonResponse({'id_list':id_list})

def latest(request):
    latest_event=Event.objects.order_by('-create_date').first()
    others_list = [
        {
            "title": other.title,
            "description": other.description,
        }
        for other in latest_event.others.all()
    ]
    if latest_event:
        return JsonResponse({
            'id': latest_event.id,
            'title': latest_event.title,
            'dates':[latest_event.start_date,latest_event.end_date],
            'location': latest_event.location,
            'map': latest_event.place,
            'images':[latest_event.images_top.url if latest_event.images_top else None,
                      latest_event.images_top.url if latest_event.images_top else None],
            'others': others_list,
            'leagues': latest_event.leagues,
        })
    else:
        return JsonResponse({'error': 'No events found'}, status=404)