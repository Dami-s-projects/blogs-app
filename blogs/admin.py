from django.contrib import admin
from .models import BlogPostTitle
from .models import BlogContent

# Register your models here.
admin.site.register(BlogPostTitle)
admin.site.register(BlogContent)