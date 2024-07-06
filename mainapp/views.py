import logging

from django.conf import settings
from django.views.generic import ListView, TemplateView

from .services.cat_api import get_cat

logger = logging.getLogger(__name__)


class HomePage(TemplateView):
    """Home page"""

    template_name = "mainapp/index.html"

    def dispatch(self, request, *args, **kwargs):
        if not request.session.session_key:
            request.session.save()
        request.session.set_expiry(settings.SESSION_COOKIE_AGE)
        return super().dispatch(request, *args, **kwargs)


class FloatFormView(TemplateView):
    """Form for cats number, htmx"""

    template_name = "mainapp/float_form.html"


class CatListView(ListView):
    """Main page with cats list"""

    template_name = "mainapp/cat_list.html"
    context_object_name = "cats"
    paginate_by = 2

    def get_queryset(self):
        """Get list of cats from get_cat()"""
        cat_num = self.request.GET.get("cat_num")
        content = get_cat(cat_num)
        logger.info(f"LOG MESSAGE: {content}")
        return content
