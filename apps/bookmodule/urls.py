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
    path("lab9/task1/", views.lab9_task1, name="lab9_task1"),
    path("lab9/task2/", views.lab9_task2, name="lab9_task2"),
    path("lab9/task3/", views.lab9_task3, name="lab9_task3"),
    path("lab9/task4/", views.lab9_task4, name="lab9_task4"),
    path("lab9/task5/", views.lab9_task5, name="lab9_task5"),
    path("lab9/task6/", views.lab9_task6, name="lab9_task6"),
    path("lab9_part1/listbooks/", views.lab10_part1_listbooks, name="lab10_part1_listbooks"),
    path("lab9_part1/addbook/", views.lab10_part1_addbook, name="lab10_part1_addbook"),
    path("lab9_part1/editbook/<int:id>/", views.lab10_part1_editbook, name="lab10_part1_editbook"),
    path("lab9_part1/deletebook/<int:id>/", views.lab10_part1_deletebook, name="lab10_part1_deletebook"),
    path("lab9_part2/listbooks/", views.lab10_part2_listbooks, name="lab10_part2_listbooks"),
    path("lab9_part2/addbook/", views.lab10_part2_addbook, name="lab10_part2_addbook"),
    path("lab9_part2/editbook/<int:id>/", views.lab10_part2_editbook, name="lab10_part2_editbook"),
    path("lab9_part2/deletebook/<int:id>/", views.lab10_part2_deletebook, name="lab10_part2_deletebook"),
    path("lab11/liststudents/", views.lab11_list_students, name="lab11_list_students"),
    path("lab11/addstudent/", views.lab11_add_student, name="lab11_add_student"),
    path("lab11/editstudent/<int:id>/", views.lab11_edit_student, name="lab11_edit_student"),
    path("lab11/deletestudent/<int:id>/", views.lab11_delete_student, name="lab11_delete_student"),

    path("lab11/liststudents2/", views.lab11_list_students2, name="lab11_list_students2"),
    path("lab11/addstudent2/", views.lab11_add_student2, name="lab11_add_student2"),
    path("lab11/editstudent2/<int:id>/", views.lab11_edit_student2, name="lab11_edit_student2"),
    path("lab11/deletestudent2/<int:id>/", views.lab11_delete_student2, name="lab11_delete_student2"),

    path("lab11/listimages/", views.lab11_list_images, name="lab11_list_images"),
    path("lab11/addimage/", views.lab11_add_image, name="lab11_add_image"),
    path("lab11/deleteimage/<int:id>/", views.lab11_delete_image, name="lab11_delete_image"),
    path('users/register/', views.registerUser, name='register'),


]