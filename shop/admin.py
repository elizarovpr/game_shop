from django.contrib import admin

from .models import Product, Requirement, Genre


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'year', 'price']
    prepopulated_fields = {'slug': ['title']}


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}


@admin.register(Requirement)
class RequirementAdmin(admin.ModelAdmin):
    pass
