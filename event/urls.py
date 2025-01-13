from django.urls import path
from . import views

urlpatterns = [
    path("", views.events, name="events"),
    path("latest/", views.latest, name="latest"),
    path("<str:event_id>/", views.event_info, name="event_info"),
]
