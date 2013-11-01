from django.contrib import admin
from tweety.models import Post

class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title']}),
        ('Content',          {'fields': ['body']}),
        ('Date information', {'fields': ['pub_date']}),
        ('Popularity',      {'fields': ['likes'], 'classes': ['collapse']}),
    ]
admin.site.register(Post, PostAdmin)