from django.views.generic import TemplateView


class MainPageView(TemplateView):
    """Главная страница"""

    template_name = "base.html"
