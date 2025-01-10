from django.http import JsonResponse
from .models import Event

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
            'poster_top': latest_event.poster_top.url if latest_event.poster_top else None,
            'poster_bottom': latest_event.poster_bottom.url if latest_event.poster_bottom else None,
        })
    else:
        # Return an empty response if no event exists
        return JsonResponse({'error': 'No events found'}, status=404)