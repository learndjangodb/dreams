from django.contrib import admin
from .models import DreamReal, Online, Author, Book


# Register your models here.
class CmpAdmin(admin.ModelAdmin):
    lisi_dispaly = ('name', 'email', 'phonenumber')


admin.site.register(DreamReal, CmpAdmin)


@admin.register(Author)
class AdminAuthor(admin.ModelAdmin):
    list_display = ['title', 'name', 'birth_date']
