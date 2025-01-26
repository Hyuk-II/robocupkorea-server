from django.urls import path
from . import views

urlpatterns = [
    path("", views.GetNotices.as_view()),
    path("<str:notice_id>", views.GetNotice.as_view()),
    path("files/<str:pdf_name>", views.Download.as_view()),
]
