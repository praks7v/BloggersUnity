from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, BlogPost, ContactMessage


# Register your models with the Django admin site.

# Register the CustomUser model with an extended UserAdmin configuration.
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'date_joined')
    list_filter = ('is_active', 'is_staff', 'date_joined')
    search_fields = ('username', 'email', 'first_name', 'last_name')


admin.site.register(CustomUser, CustomUserAdmin)


# Register the BlogPost model with a customized admin configuration.
class BlogPostAdmin(admin.ModelAdmin):
    list_filter = ('status', 'categories')


admin.site.register(BlogPost, BlogPostAdmin)


# Register the ContactMessage model with a customized admin configuration.
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'subject')
    list_filter = ('subject',)
    search_fields = ('first_name', 'last_name', 'email')


admin.site.register(ContactMessage, ContactMessageAdmin)
