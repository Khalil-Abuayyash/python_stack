from django.shortcuts import redirect, render
from .models import Book, Author

# Create your views here.
def index(request):
    pass

def show_all_books(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'books.html', context)

def show_book_details(request, id):
    context = {
        'book': Book.objects.get(id=id),
        'authors': Author.objects.all()
    }
    return render(request, 'book_details.html', context)

def add_book(request):

    title = request.POST['title']
    desc = request.POST['desc']
    Book.objects.create(title=title, desc=desc)
    return redirect('/books')

def add_author_to_book(request, book_id):
    book = Book.objects.get(id=book_id)
    author = Author.objects.get(id=request.POST['author_id'])
    book.authors.add(author)
    return redirect(f'/books/{book_id}')

def show_all_authors(request):
    context = {
        'authors': Author.objects.all()
    }
    return render(request, 'authors.html', context)

def show_author_details(request, id):
    context = {
        'author': Author.objects.get(id=id),
        'books': Book.objects.all()
    }
    return render(request, 'author_details.html', context)

def add_author(request):

    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    notes = request.POST['notes']
    Author.objects.create(first_name=first_name, last_name=last_name,notes=notes)
    return redirect('/authors')

def add_book_to_author(request, author_id):
    author = Author.objects.get(id=author_id)
    book = Book.objects.get(id=request.POST['book_id'])
    author.books.add(book)
    return redirect(f'/authors/{author_id}')