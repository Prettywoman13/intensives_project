from django.urls import path

from .views import FeedBack

app_name = "feedback"

urlpatterns = [path("", FeedBack.as_view(), name="main")]
