from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import CustomUser, BlogPost  # Import your model


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'date_joined')
    list_filter = ('is_active', 'is_staff', 'date_joined')
    search_fields = ('username', 'email', 'first_name', 'last_name')


admin.site.register(CustomUser, CustomUserAdmin)


class BlogPostAdmin(admin.ModelAdmin):
    list_filter = ('status', 'categories', 'tags')
    # Other admin options and customizations, if needed


admin.site.register(BlogPost, BlogPostAdmin)
