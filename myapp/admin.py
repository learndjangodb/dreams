from django.contrib import admin
from .models import DreamReal, Online, Author, Book, OpinionPoll, Response


# Register your models here.
class CmpAdmin(admin.ModelAdmin):
    lisi_dispaly = ('name', 'email', 'phonenumber')


admin.site.register(DreamReal, CmpAdmin)


@admin.register(Author)
class AdminAuthor(admin.ModelAdmin):
    list_display = ['title', 'name', 'birth_date']


@admin.register(Book)
class AdminBook(admin.ModelAdmin):
    list_display = ['name']


@admin.register(OpinionPoll)
class AdminPoll(admin.ModelAdmin):
    list_display = ['question', 'poll_date']


@admin.register(Response)
class AdminResonse(admin.ModelAdmin):
    list_display = ['person_name', 'response']
    list_filter = ['poll', 'person_name']
