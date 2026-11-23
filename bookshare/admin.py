from django.contrib import admin
from .models import Book, Category, City, Share


admin.site.register(Book)
admin.site.register(Category)
admin.site.register(City)
admin.site.register(Share)