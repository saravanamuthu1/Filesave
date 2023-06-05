from django.contrib import admin
from .models import User,Post
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=['userName','password']
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'file_field']