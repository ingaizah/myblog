from django.contrib import admin
from myblog.models import Post

# Register your models here.
admin.site.register(Post)

class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':['title']}),
        (None, {'fields':['text']}),

        ]
