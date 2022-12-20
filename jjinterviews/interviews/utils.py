from random import choice
from typing import List

from .models import Pack, Question


def create_pack(questions: List[Question]) -> Pack:
    """
    Функция генерации пака вопросов
    """
    questions_iter = iter(questions)
    first = next(questions_iter)
    new_pack = Pack()
    new_pack.save()
    first_id = 0
    curr_theme = first.theme
    for i, question in enumerate(questions_iter, start=1):
        if curr_theme != question.theme:
            new_pack.questions.add(choice(questions[first_id:i]))
            first_id = i
            curr_theme = question.theme

    new_pack.questions.add(choice(questions[first_id:]))
    return new_pack
