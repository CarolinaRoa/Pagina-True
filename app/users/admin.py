""" Admin site for Users """

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
#models
#from django.contrib.auth.models import User
from users.models import UserProfile


# Register your models here.

class UserAdmin(admin.ModelAdmin):
    """Profile admin"""
    
    readonly_fields = ('created', 'modified')
    

admin.site.register(UserProfile, UserAdmin)

    
