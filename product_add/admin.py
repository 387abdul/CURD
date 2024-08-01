from django.contrib import admin
from .models import Create
# Register your models here.
@admin.register(Create)
class CreateAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'image')
    search_fields = ('name', 'description')