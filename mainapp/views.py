from django.views.generic import TemplateView

from .services.cat_api import get_cat


class MainPageView(TemplateView):
    """Главная страница"""

    template_name = "base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cat_url = get_cat()
        context["cat_url"] = cat_url
        return context
