from django.contrib import admin
from freeshelfapp.models import Book , Author , Category 
# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_added',)
    list_filter = ('date_added', 'author',)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display=('last_name', 'first_name',)
    fields = ['first_name', 'last_name']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')