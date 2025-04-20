
from django.urls import path

from .import views

urlpatterns = [

    path('', views.home, name="home"),
    path('books', views.all_books, name="books"),
    path('deletebook/<int:pk>', views.remove_book, name="removebook"),
    path('edit/<int:pk>', views.edit_book, name="editbook"),
    path('update/<int:pk>', views.update_book, name="updatebook"),

]
