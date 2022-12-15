from django.urls import path

from .views import AboutView

app_name = "homepage"

urlpatterns = [path("", AboutView.as_view(), name="main")]
