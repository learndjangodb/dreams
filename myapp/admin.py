from django.contrib import admin
from .models import DreamReal, Online, Author, Book, OpinionPoll, Response, Person, Human


# Register your models here.
class CmpAdmin(admin.ModelAdmin):
    lisi_dispaly = ('name', 'email', 'phonenumber')


admin.site.register(DreamReal, CmpAdmin)


@admin.register(Author)
class AdminAuthor(admin.ModelAdmin):
    list_display = ['title', 'name', 'birth_date']
    empty_value_display = '-empty-'


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


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'colored_name')


@admin.register(Human)
class HumanAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'sex']
