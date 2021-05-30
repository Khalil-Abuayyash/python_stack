from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('login', views.login),
    path('books', views.welcome),
    path('logout', views.logout),
    path('add', views.add_book),
    path('books/<int:book_id>', views.show_book_details),
    path('add_to_fav/<int:book_id>', views.add_to_fav),
    path('update/<int:book_id>', views.edit),
    path('destroy/<int:book_id>', views.delete),
]