from django.shortcuts import redirect
from django.views.generic import FormView

from .forms import build_create_interview_form


class CreateInterview(FormView):
    template_name = "pages/interviews/create.html"
    form_class = build_create_interview_form()

    def form_valid(self, form):
        # Сюда добавить логик
        print(form.cleaned_data)
        return redirect("interviews:create")
