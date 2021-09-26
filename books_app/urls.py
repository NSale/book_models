from django.urls import path
from . import views

urlpatterns = [
    path('books', views.index, name='books'),
    path('books/<int:book_id>', views.book_details, name='book_details')
]
