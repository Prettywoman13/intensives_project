from django.urls import path

from .views import CreateInterview, interview_view

app_name = "interview"

urlpatterns = [
    path("new/", CreateInterview.as_view(), name="create"),
    path("interview/<uuid:interview_id>", interview_view, name="interview"),
]
