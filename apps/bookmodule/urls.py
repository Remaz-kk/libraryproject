from django.urls import path
from . import views

app_name = "books"  

urlpatterns = [
    path("", views.index, name="index"),
    path("listbooks/", views.listbooks, name="listbooks"),
    path("aboutus/", views.aboutus, name="aboutus"),
    path("<int:bookId>/", views.onebook, name="onebook"),
]