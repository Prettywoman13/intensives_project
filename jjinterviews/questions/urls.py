from django.urls import path

from .views import NewQuestion

app_name = "questions"

urlpatterns = [path("new_question/", NewQuestion.as_view(), name="new")]
