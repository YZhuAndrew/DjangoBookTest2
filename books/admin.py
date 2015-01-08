from django.contrib import admin
from books.models import *

# Register your models here.


class PublisherAdmin(admin.ModelAdmin):
    # pass
    # fields = ('name', 'country', 'website')
    list_display = ('name', 'country', 'website')

admin.site.register(Publisher, PublisherAdmin)


class AuthorAdmin(admin.ModelAdmin):
    # pass
    list_display = ('first_name', 'last_name', 'country')
admin.site.register(Author, AuthorAdmin)


class BookAdmin(admin.ModelAdmin):
    # pass
    list_display = ('title', 'publisher')
admin.site.register(Book, BookAdmin)
