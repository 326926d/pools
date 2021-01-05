from django.contrib import admin
from . import models 
from .models import GeeksModel, Tutors, Book, Author

@admin.register(Tutors)
class TutorsAdmin(admin.ModelAdmin):
    pass
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(GeeksModel)
# Register your models here.
