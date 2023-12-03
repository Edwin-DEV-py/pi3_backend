from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

#vista personalizada de admin
class CustomUserAdmin(UserAdmin):
    filter_horizontal = ()
    list_display = ['email', 'names', 'last_names','is_superuser','is_active']
    list_filter = ['is_staff', 'is_superuser', 'is_active']
    search_fields = ('email', 'names', 'last_names')
    ordering = ('email',)
    
    
admin.site.register(User,CustomUserAdmin)
