from django.views.generic import FormView

from .forms import CreateInterviewForm


class CreateInterview(FormView):
    template_name = "pages/interviews/create.html"
    form_class = CreateInterviewForm
