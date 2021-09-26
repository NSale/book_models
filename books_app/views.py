from django.shortcuts import render, get_object_or_404
from django.db.models import Avg

from .models import Book


# Create your views here.
def index(request):
    books = Book.objects.all().order_by('-rating')
    num_books = books.count()
    avg_rating = books.aggregate(Avg('rating'))
    return render(request, 'books_app/index.html', {
        'books': books,
        'total_number_of_books': num_books,
        'average_rating': avg_rating['rating__avg'],
    })


def book_details(request, slug):
    # Depricated
    # try:
    #     book = Book.objects.get(id=book_id)
    # except Exception as e:
    #     raise Http404('There is no book with that index')
    book = get_object_or_404(Book, slug=slug)
    return render(request, 'books_app/book_detail.html', {
        'book': book,
    })
