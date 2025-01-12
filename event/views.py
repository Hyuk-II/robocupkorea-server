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
    if latest_event:
        return JsonResponse({
            'id': latest_event.id,
            'title': latest_event.title,
            'create_date': latest_event.create_date,
            'start_date': latest_event.start_date,
            'end_date': latest_event.end_date,
            'location': latest_event.location,
            'place': latest_event.place,
            'leagues': latest_event.leagues,
            'images_top': latest_event.images_top.url if latest_event.images_top else None,
            'images_bottom': latest_event.images_top.url if latest_event.images_top else None,
        })
    else:
        return JsonResponse({'error': 'No events found'}, status=404)