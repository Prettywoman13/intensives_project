from django.shortcuts import redirect
from django.views.generic import FormView

from .forms import build_create_interview_form


class CreateInterview(FormView):
    template_name = "pages/interviews/create.html"
    form_class = build_create_interview_form()

    def get(self, request, *args: str, **kwargs):
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        # Сюда добавить логику
        print(form.cleaned_data)
        return "ok"

    def post(self, request, *args: str, **kwargs):
        super().post(request, *args, **kwargs)
        return redirect("interviews:create")
