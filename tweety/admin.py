from django.contrib import admin
from tweety.models import Post
from tweety.models import User

admin.site.register(User)

class UserInline(admin.TabularInline):
    model = User
    extra = 1
    

class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title']}),
        ('Content',          {'fields': ['body']}),
        ('Date information', {'fields': ['pub_date']}),
        ('Popularity',      {'fields': ['likes'], 'classes': ['collapse']}),
    ]
    inlines = [UserInline]
    list_display = ('title', 'body', 'pub_date', 'likes', 'was_published_recently')
admin.site.register(Post, PostAdmin)
