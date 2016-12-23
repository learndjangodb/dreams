from django.contrib import admin
from .models import DreamReal, Online

# Register your models here.
class CmpAdmin(admin.ModelAdmin):
	lisi_dispaly = ('name', 'email', 'phonenumber')

admin.site.register(DreamReal, CmpAdmin)

