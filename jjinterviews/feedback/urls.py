from django.urls import path

from .views import feedback

app_name = "feedback"

urlpatterns = [path("", feedback, name="main")]
