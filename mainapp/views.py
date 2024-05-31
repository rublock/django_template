from django.views.generic import ListView, TemplateView

from .services.cat_api import get_cat


class HomePage(TemplateView):
    """Home page"""

    template_name = "mainapp/index.html"


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
        return content
