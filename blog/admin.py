from csv import list_dialects
from xml.etree.ElementTree import Comment
from django.contrib import admin
from blog.models import Post, Subject, Category, Comment

# Register your models here.

class SubjectAdminInlines(admin.TabularInline):
	#Tabular/Stacked
	model = Comment
	fileds = ['name', 'subject', 'message']
	extra = 0

class CommentAdmin(admin.ModelAdmin):
	list_display = ['name', 'created_time', 'status']
	search_fields = ['subject', 'message']

class PostAdmin(admin .ModelAdmin):
	list_display = ['id', 'title', 'Active', 'updated_time', 'Age']
	search_filter = ['content', 'title']
	list_filter = ('Active', 'Age')
	date_hierarchy = 'created_time'
	list_display_links = ['id', 'title']
	fileds = ['title']
	#inlines = [CommentAdminInlines]
	#exclude = []
	#ordering = ['-updated_time']

	#def has_change_permission(self, request, obj=None):
	#	return False

	#def has_add_permission(self, request, obj=None):
	#	return False

	#def has_delete_permission(self, request, obj=None):
	#	return False



admin.site.register(Post,PostAdmin)
admin.site.register(Subject) 	
admin.site.register(Category)
admin.site.register(Comment, CommentAdmin)