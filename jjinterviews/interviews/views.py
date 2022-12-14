from django.views.generic import FormView

from .forms import build_create_interview_form


class CreateInterview(FormView):
    template_name = "pages/interviews/create.html"
    form_class = build_create_interview_form()
