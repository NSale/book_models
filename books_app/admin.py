from django.contrib import admin

from .models import Book, Author, Address, Country


# Register your models here.
class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ['slug', ] - need to remove this, because prepopulated_fields wouldn't work with readonly field
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('author', 'rating')
    list_display = ('title', 'author', 'rating', 'is_bestselling')
    search_fields = ('author', 'title')


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'address')
    list_filter = ('last_name',)


class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    list_filter = ('name',)

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Address)
admin.site.register(Country, CountryAdmin)
