from django.views.generic.base import TemplateView


class AboutView(TemplateView):
    template_name = "pages/homepage/main.html"
