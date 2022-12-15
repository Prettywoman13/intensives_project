from django.urls import path

from .views import CreateInterview

app_name = "interview"

urlpatterns = [path("", CreateInterview.as_view(), name="create")]
