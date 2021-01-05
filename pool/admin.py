from django.contrib import admin
from . import models 
from .models import Tutors, Book, Author

@admin.register(Tutors)
class TutorsAdmin(admin.ModelAdmin):
    pass
admin.site.register(Book)
admin.site.register(Author)
# Register your models here.
