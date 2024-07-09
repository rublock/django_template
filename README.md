### BASE DJANGO TEMPLATE
### MAINAPP

- [x] .gitignore python
- [x] MIT License 
- [x] mainapp
- [x] .env and sample.env
- [x] BASE_DIR / "templates"
- [x] mainapp/services
- [x] requirements/local.txt
---
- [x] htmx, bootstarp5, static, header, sticky footer
- [x] HomePage View
- [x] List View
- [x] pagination
- [ ] 18in
- [x] logging
- [ ] docs
- [ ] degug toolbar
- [x] context processors
- [x] admin
- [ ] load roller async
- [ ] form
- [ ] test all!
- [ ] exceptions, 404 page
- [x] session id
- [x] models
- [ ] htmx to readme
---
### HomePage View
```python
class HomePage(TemplateView):
    """Home page"""
    
    template_name = "mainapp/index.html"
```
### CatList View
```python
from .services.cat_api import get_cat


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
```
### Pagination
```html
<ul class="list-unstyled" >
    {% for i in cats %}
        <div class="d-flex justify-content-center align-items-center">
            <img src="{{ i }}" alt="Cat Photo" width="240" height="160">
        </div>
        <br>
    {% endfor %}

    <!-- Pagination -->
    {% if page_obj.paginator.num_pages > 1 %}
      <nav aria-label="Page navigation example" class="d-flex justify-content-center align-items-center">

        <ul class="pagination">
            {% if page_obj.has_previous %}
              <li class="page-item"><a class="page-link" href="?page={{ page_obj.previous_page_number }}">Previous</a></li>
            {% endif %}

            {% for i in page_obj.paginator.page_range %}
              {% if page_obj.number == i %}
                <li class="page-item"><a class="page-link" href="?page={{ i }}"> {{ i }} </a></li>
              {% elif i > page_obj.number|add:"-3" and i < page_obj.number|add:"3" %}
                <li class="page-item"><a class="page-link" href="?page={{ i }}"> {{ i }} </a></li>
              {% endif %}
            {% endfor %}

            {% if page_obj.has_next %}
              <li class="page-item"><a class="page-link" href="?page={{ page_obj.next_page_number }}">Next</a></li>
            {% endif %}
        </ul>

      </nav>
    {% endif %}
    <!-- END Pagination -->

</ul>
```
### Session
```python
class HomePage(TemplateView):
    """Home page"""

    template_name = "mainapp/index.html"

    def dispatch(self, request, *args, **kwargs):
        if not request.session.session_key:
            request.session.save()
        request.session.set_expiry(settings.SESSION_COOKIE_AGE)
        return super().dispatch(request, *args, **kwargs)
```
config/settings.py
```python
SESSION_COOKIE_AGE = 60 * 60 * 24 * 30
```
to get session id
```python
session_id = request.session.session_key
```
![](https://github.com/rublock/django_template/raw/main/static/img/sessionid.png)
### Logging
config/settings.py
```txt
1. CRITICAL. Цифровой эквивалент — 50.
2. ERROR. Цифровой эквивалент — 40.
3. WARNING. Цифровой эквивалент — 30.
4. INFO. Цифровой эквивалент — 20.
5. DEBUG. Цифровой эквивалент — 10.
6. NOTSET. Цифровой эквивалент — 0.
```
```python
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "console": {"format": "[%(asctime)s] %(levelname)s %(name)s (%(lineno)d) %(message)s"},
    },
    "handlers": {
        "console": {"class": "logging.StreamHandler", "formatter": "console"},
    },
    "loggers": {
        "django": {"level": "INFO", "handlers": ["console"], },
        "mainapp": {"level": "INFO", "handlers": ["console"], },
    },
}
```
```python
import logging

logger = logging.getLogger(__name__)

class CatListView(ListView):
    """Main page with cats list"""

    template_name = "mainapp/cat_list.html"
    context_object_name = "cats"
    paginate_by = 2

    def get_queryset(self):
        """Get list of cats from get_cat()"""
        cat_num = self.request.GET.get("cat_num")
        content = get_cat(cat_num)
        logger.info(f'LOG MESSAGE: {content}')
        return content
```
![](https://github.com/rublock/django_template/raw/main/static/img/logging.png)

---
![](https://github.com/rublock/django_template/raw/main/static/img/mainapp.png)