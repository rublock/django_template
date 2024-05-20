from django.views.generic import TemplateView

from .services.cat_api import get_cat


class MainPageView(TemplateView):
    """Главная страница"""

    template_name = "mainapp/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cat_img = get_cat()
        context["cat_img"] = cat_img
        context["title"] = "cats"
        return context
