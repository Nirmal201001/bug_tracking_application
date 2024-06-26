from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class UserModel(UserAdmin):
    list_display = ['username', 'email', 'user_type']


admin.site.register(CustomUser, UserModel)
admin.site.register(customer)
admin.site.register(staff)
admin.site.register(bug_report)
admin.site.register(bug_status)  
