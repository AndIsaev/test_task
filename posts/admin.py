from django.contrib import admin
from .models import Post, Follow


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Model Post for admin-user."""
    fields = ("author", "title", "text", "pub_date", 'read_post')
    search_fields = ("text",)
    readonly_fields = ("pub_date", )
    list_filter = ("pub_date",)
    empty_value_display = "-пусто-"


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    """Model Follow for subscribe."""
    fields = ("author", "user",)
    search_fields = ("author",)
    empty_value_display = "-пусто-"
