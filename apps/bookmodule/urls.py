from django.urls import path
from . import views

app_name = "books"

urlpatterns = [
    path("", views.index, name="index"),
    path("listbooks/", views.listbooks, name="listbooks"),
    path("aboutus/", views.aboutus, name="aboutus"),
    path("<int:bookId>/", views.onebook, name="onebook"),
    path("html5/listing/", views.html5_listing, name="html5_listing"),
    path("html5/tables/", views.html5_tables, name="html5_tables"),
    path("html5/links/", views.html5_links, name="html5_links"),
    path("html5/text/formatting/", views.html5_text_formatting, name="html5_text_formatting"),
    path("search/", views.search, name="search"),
    path("simple/query", views.simple_query, name="simple_query"),
    path("complex/query/", views.lookup_query, name="lookup_query"),
    path("lab8/task1/", views.lab8_task1, name="lab8_task1"),
    path("lab8/task2/", views.lab8_task2, name="lab8_task2"),
    path("lab8/task3/", views.lab8_task3, name="lab8_task3"),
    path("lab8/task4/", views.lab8_task4, name="lab8_task4"),
    path("lab8/task5/", views.lab8_task5, name="lab8_task5"),
    path("lab8/task7/", views.lab8_task7, name="lab8_task7"),
    
]