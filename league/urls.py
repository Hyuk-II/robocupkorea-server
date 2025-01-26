from django.urls import path
from . import views

urlpatterns = [
    path("", views.GetLeagues.as_view()),
    path("<str:league_id>", views.GetLeague.as_view()),
    path("<str:league_id>/attachments/meta", views.GetAttachments.as_view()),
    path("files/<str:pdf_name>", views.Download.as_view()),
]
