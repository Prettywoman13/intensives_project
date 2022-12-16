from random import choice

from django.views.generic import FormView, ListView
from django.shortcuts import redirect

from questions.models import Question
from .forms import build_create_interview_form
from .models import Pack


class CreateInterview(FormView):
    template_name = "pages/interviews/create.html"
    form_class = build_create_interview_form()

    def form_valid(self, form):
        del form.cleaned_data["Почта"]
        ids_list = [
            int(id) for sublist in form.cleaned_data.values() for id in sublist
        ]
        new_pack = Pack()
        new_pack.save()
        for theme_id in ids_list:
            questions = Question.objects.all().filter(theme=theme_id)
            new_pack.questions.add(choice(questions))
        return redirect("interviews:create")
