from django.contrib import admin

from .models import Book, Author


# Register your models here.
class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ['slug', ] - need to remove this, because prepopulated_fields wouldn't work with readonly field
    prepopulated_fields = {'slug': ('title', )}
    list_filter = ('author', 'rating')
    list_display = ('author', 'title', 'rating', 'is_bestselling')
    search_fields = ('author', 'title')


admin.site.register(Book, BookAdmin)
admin.site.register(Author)
