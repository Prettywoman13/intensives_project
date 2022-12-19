from django.urls import path

from .views import test

app_name = "statistic"

urlpatterns = [path("", test, name="main")]
