from django.contrib import admin
from django.urls import include, path
from interviews.views import register


app_name = "interviews"

urlpatterns = [
    path("", register),
]
