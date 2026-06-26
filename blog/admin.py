from django.contrib import admin
from blog.models import Post, Category
from django_summernote.admin import SummernoteModelAdmin

#@admin.register(Post)     ham in doroste hm paeini
class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty'
    list_display = ('title', 'author',  'created_date', 'status', 'counted_view', 'published_date')
    list_filter = ('status','author')
    search_fields = ['title', 'content']
    summernote_fields = ('content',)
    

admin.site.register(Category)
admin.site.register(Post, PostAdmin) #-ham in doroste hm decorator