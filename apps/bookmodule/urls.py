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
    
    
]