from django.urls import path

from mainapp.apps import MainappConfig
from mainapp.views import FloatFormView, CatListView, HomePage

app_name = MainappConfig.name

urlpatterns = [
    path("", HomePage.as_view(), name="home"),
    path("cat_list/", CatListView.as_view(), name="cat_list"),
    path("float_form/", FloatFormView.as_view(), name="float_form"),
]
