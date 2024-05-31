from django.urls import path

from mainapp import views
from mainapp.apps import MainappConfig
from mainapp.views import FloatFormView

app_name = MainappConfig.name

urlpatterns = [
    path("", views.HomePage.as_view(), name="home_page"),
    path("cat_list/", views.CatList.as_view(), name="cat_list_page"),
    path("float_form/", FloatFormView.as_view(), name="float_form"),
]
