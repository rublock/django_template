import logging

from django.conf import settings
from django.shortcuts import redirect
from django.views.generic import ListView, TemplateView

from .models import Session, SessionUrl
from .services.cat_api import get_cat

logger = logging.getLogger(__name__)


class HomePage(TemplateView):
    """Home page"""
    template_name = "mainapp/index.html"
    context_object_name = "cats"
    paginate_by = 2

    def get(self, request, *args, **kwargs):
        """
        Метод проверяет есть ли ключ сессии в браузере (Application - Cookie),
        если его нет, то ключ устанавливается.
        Устанавливается на какой срок действует ключ.
        Проверяется есть ли уже такой ключ, если нет то
        ключ сохраняется в таблицу Session.
        Проверяется есть ли в БД записи с url изображений котов согласно
        ключу сессии. Если есть-то редирект на cat_list/.
        Если нет-то открывается главная страница
        """
        if not request.session.session_key:
            request.session.create()
            request.session.set_expiry(settings.SESSION_COOKIE_AGE)

        sessionid = request.session.session_key

        if not Session.objects.filter(key=sessionid).exists():
            data = Session.objects.create(key=sessionid)
            data.save()

        key = Session.objects.get(key=sessionid)
        id = key.id
        if SessionUrl.objects.filter(session_key_id=id).exists():
            return redirect('cat_list/')
        else:
            return super().get(request, *args, **kwargs)


class FloatFormView(TemplateView):
    """Форма на htmx, для запроса количества котов"""

    template_name = "mainapp/float_form.html"


class CatListView(ListView):
    """Страница с котами"""

    template_name = "mainapp/cat_list.html"
    context_object_name = "cats"
    paginate_by = 2

    def get_queryset(self):
        """
        Метод проверяет есть ли uls котов в БД по ключу сесссии.
        Если есть-то отправляет в браузер content со списком url котов.
        Если нет-то запрашивает сервис API get_cat() и добавляет url в БД.
        Отправляет в браузер content со списком url котов из БД.
        """
        sessionid = self.request.session.session_key
        session = Session.objects.get(key=sessionid)
        content = []
        key = Session.objects.get(key=sessionid)
        id = key.id

        if SessionUrl.objects.filter(session_key_id=id).exists():
            urls = SessionUrl.objects.filter(session_key_id=id)
            for i in urls:
                content.append(i.url)
            return content

        else:
            cat_num = self.request.GET.get("cat_num")
            content = get_cat(cat_num)
            logger.info(f"LOG MESSAGE: {content}")
            for i in content:
                if not SessionUrl.objects.filter(session_key=session, url=i).exists():
                    url = SessionUrl(session_key=session, url=i)
                    url.save()
            return content
