from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_leagues, name="get_leagues"),
    path("<str:league_id>/", views.get_league, name="get_league"),
    path(
        "<str:league_id>/attachments/meta/",
        views.get_attachments,
        name="get_attachments",
    ),
    path("files/<str:pdf_name>/", views.download, name="download"),
]
