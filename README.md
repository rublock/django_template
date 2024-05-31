### BASE DJANGO TEMPLATE
##### Mainapp

- [ ] HomePage View
- [ ] 18in
- [ ] logging
- [ ] docs
- [ ] degug toolbar
- [x] context processors
- [ ] admin
- [ ] load roller async
- [x] cat form
- [ ] exceptions

* .gitignore python
* MIT License
* mainapp
* .env and sample.env
* BASE_DIR / "templates"
* mainapp/services
* requirements/local.txt
* htmx, bootstarp5, static, header, sticky footer
---
* HomePage View
```python
class HomePage(TemplateView):
    template_name = "mainapp/index.html"
```
* CatList View
```python
class CatList(ListView):
    """Main page with cats list"""
    template_name = "mainapp/cat_list.html"
    context_object_name = "cats"
    paginate_by = 2

    def get_queryset(self):
        """Get list of cats from get_cat()"""
        content = get_cat()
        return content
```
* pagination
```html
<ul class="list-unstyled" >
    {% for i in cats %}
        <div class="d-flex justify-content-center align-items-center">
            <img src="{{ i }}" alt="Cat Photo" width="240" height="160">
        </div>
        <br>
    {% endfor %}

    <!-- Pagination -->
      <nav aria-label="Page navigation example" class="d-flex justify-content-center align-items-center">

        <ul class="pagination">
            {% if page_obj.has_previous %}
              <li class="page-item"><a class="page-link" href="/?page={{ page_obj.previous_page_number }}">Previous</a></li>
            {% endif %}

            {% for i in page_obj.paginator.page_range %}
              {% if page_obj.number == i %}
                <li class="page-item"><a class="page-link" href='?page={{ i }}'> {{ i }} </a></li>
              {% elif i > page_obj.number|add:'-3' and i < page_obj.number|add:'3' %}
                <li class="page-item"><a class="page-link" href='?page={{ i }}'> {{ i }} </a></li>
              {% endif %}
            {% endfor %}

            {% if page_obj.has_next %}
              <li class="page-item"><a class="page-link" href="/?page={{ page_obj.next_page_number }}">Next</a></li>
            {% endif %}
        </ul>

      </nav>
    <!-- END Pagination -->

</ul>
```
 
![](https://raw.githubusercontent.com/rublock/django_CBV/main/static/img/mainapp.png?token=GHSAT0AAAAAACSKVAFHDNURLGAFLT2FIYSEZSNZ3HQ)