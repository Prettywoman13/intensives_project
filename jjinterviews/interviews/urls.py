from django.urls import path
from interviews.views import register

app_name = "interviews"

urlpatterns = [
    path("", register),
]
