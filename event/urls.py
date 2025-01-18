from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_events, name="get_events"),
    path("latest/", views.latest, name="latest"),
    path("tests/", views.test, name="test"),
    path("<str:event_id>/", views.get_event, name="get_event"),
]
