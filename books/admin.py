from django.contrib import admin

from .models import Author, Book, Hist, Dict, Artc,Pros
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Hist)
admin.site.register(Artc)
admin.site.register(Dict)
admin.site.register(Pros)

# Register your models here.
