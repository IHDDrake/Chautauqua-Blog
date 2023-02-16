from django.contrib import admin
from .models import Post, Comment

# Registering models
admin.site.register(Post)
admin.site.register(Comment)
