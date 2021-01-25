from django.contrib import admin
from .models import Blog

# Admin options
class BlogAdmin(admin.ModelAdmin):
	list_display = ['id', 'author', 'title', 'dop']
	list_editable = ['title']
	ordering = ['-title']
	list_filter = ['dop']
	search_fields = ['title', 'author']
	list_per_page = 3

admin.site.register(Blog, BlogAdmin)
