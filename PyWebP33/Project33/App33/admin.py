from django.contrib import admin
from .models import *

# Register your models here.
# моделі, зареєстровані у даному файлі, автоматично потрапляють
# до панелі адміністратора

class RoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'create_level', 'read_level', 'update_level', 'delete_level')

@admin.register(AccessLog)
class AccessLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'access_datetime', 'response_code')

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')

class AccessAdmin(admin.ModelAdmin):
    list_display = ('login', 'user', 'role')

admin.site.register(User, UserAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(Access, AccessAdmin)