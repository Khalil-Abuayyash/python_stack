from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('books', views.show_all_books),
    path('books/<int:id>', views.show_book_details),
    path('books/add_book', views.add_book),
    path('books/author_to_book/<int:book_id>', views.add_author_to_book),
    path('authors', views.show_all_authors),
    path('authors/<int:id>', views.show_author_details),
    path('authors/add_author', views.add_author),
    path('authors/book_to_author/<int:author_id>', views.add_book_to_author),
]