from django.contrib import admin
from .models import Book, Author, Photo, Request, Customer

# Register your models here.
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Photo)
admin.site.register(Request)
admin.site.register(Customer)
