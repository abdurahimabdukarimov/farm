from django.contrib import admin
from .models import Product, Team, Blog, Contact, News

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price"]
    prepopulated_fields = {"slug": ["name"]}

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ["name", "job"]

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ["bio", "date"]

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["name", "email"]

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ["email"]