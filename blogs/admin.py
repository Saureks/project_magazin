from django.contrib import admin

from blogs.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "is_published", "views_count",)