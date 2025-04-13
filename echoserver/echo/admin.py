from django.contrib import admin
from .models import Cat


# Register your models here.
@admin.register(Cat)
class CatAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'year_of_birth')
