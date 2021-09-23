from django.contrib import admin
from apps.users.models import *
from django.contrib.auth.models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class DocumentTypeAdmin(admin.ModelAdmin):
    list_display = ['name',]
    search_fields = ['name']

class GenderAdmin(admin.ModelAdmin):
    list_display = ['name',]
    search_fields = ['name']

class Extended_UserAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'document_number',
        'phone1',
        'phone2',
        'address',
        'photo',
        'document_type',
        'date_birth',
        'description_address',
        'gender',
    ]
    search_fields = ['user','document_number']

class UserResource(ImportExportModelAdmin):
    list_display = [
        'user',
        'document_number',
        'phone1',
        'phone2',
        'address',
        'photo',
        'document_type',
        'date_birth',
        'description_address',
        'gender',
    ]
    search_fields = ['user','document_number']
admin.site.register(DocumentType,DocumentTypeAdmin)

admin.site.register(Gender,GenderAdmin)

# admin.site.register(Extended_User,Extended_UserAdmin,)

admin.site.register(Extended_User,UserResource)