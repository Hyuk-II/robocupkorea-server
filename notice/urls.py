from django.urls import path
from . import views
#test 주석
urlpatterns = [
    path("", views.get_notices, name="get_notices"),
    path("<str:notice_id>/", views.get_notice, name="get_notice"),
    path("files/<str:pdf_name>/", views.download, name="download"),
]
