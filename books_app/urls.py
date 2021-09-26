from django.urls import path
from . import views

urlpatterns = [
    path('books', views.index, name='books'),
    path('books/<slug:slug>', views.book_details, name='book_details')
]
