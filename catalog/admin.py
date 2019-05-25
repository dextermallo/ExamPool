from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
# Register your models here.

class DepartmentAdmin(admin.ModelAdmin):
    exclude = ['sb_name']

admin.site.register(Comment)
admin.site.register(Subject)
admin.site.register(Department, DepartmentAdmin)
