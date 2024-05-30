from django.urls import path

from mainapp import views
from mainapp.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    path("", views.HomePage.as_view(), name="home_page"),
    path("cat_list", views.CatList.as_view(), name="cat_list_page"),
]
