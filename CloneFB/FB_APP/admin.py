from django.contrib import admin
from django.utils.html import format_html
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('email', 'password')
    search_fields = ('email',)

admin.site.register(UserProfile, UserProfileAdmin)
