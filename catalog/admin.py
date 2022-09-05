from django.contrib import admin
from .models import Book
# Register your models here.


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'author', 'realise_date', 'amount', 'slug')
    prepopulated_fields = {'slug': ('name',)}