from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_notices, name="get_notices"),
    path("<str:notice_id>/", views.get_notice, name="get_notice"),
    path("files/<str:pdf_name>/", views.download, name="download"),
]
