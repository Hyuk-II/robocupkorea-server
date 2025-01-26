from django.urls import path
from . import views

urlpatterns = [
    path("", views.GetEvents.as_view()),
    path("latest", views.Latest.as_view()),
    path("<str:event_id>", views.GetEvent.as_view()),
]
