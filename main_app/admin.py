from django.contrib import admin
from .models import Book, Author, Photo, BookRequest, Customer

# Register your models here.
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Photo)
admin.site.register(BookRequest)
admin.site.register(Customer)
