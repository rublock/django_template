from django.core.paginator import Paginator
from django.views.generic import ListView, TemplateView

from .services.cat_api import get_cat


class HomePage(TemplateView):
    template_name = "mainapp/index.html"


class CatList(ListView):
    """Main page with cats list"""

    template_name = "mainapp/cat_list.html"
    context_object_name = "cats"
    paginate_by = 2

    def get_queryset(self):
        """Get list of cats from get_cat()"""
        content = get_cat()
        return content
