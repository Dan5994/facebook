from django.contrib import admin
from .models import Post, Comment, UPDATED

# Register your models here.
# admin.site.register(Post)
# admin.site.register(Comment)



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ['title', 'text','counter','cotegoru']
    readonly_fields = ['cotegoru']
    search_fields = ["text__startswith"]
    ordering = ['-created_at']
    @admin.action(description="Mark selected stories as published")
    def make_published(modeladmin, request, queryset):
        queryset.update(status="p")

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    ordering = ['-created_at']
    list_display = ['text','status']
    @admin.action(description="Update")
    def make_published(modeladmin, request, queryset):
        queryset.update(status=UPDATED)