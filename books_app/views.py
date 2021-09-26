from django.shortcuts import render, get_object_or_404
from .models import Book


# Create your views here.
def index(request):
    books = Book.objects.all()
    return render(request, 'books_app/index.html', {
        'books': books,
    })


def book_details(request, book_id):
    # Depricated
    # try:
    #     book = Book.objects.get(id=book_id)
    # except Exception as e:
    #     raise Http404('There is no book with that index')
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'books_app/book_detail.html', {
        'book': book,
    })
