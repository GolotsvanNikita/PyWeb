from django.contrib import admin
from .models import *

# Register your models here.
# моделі, зареєстровані у даному файлі, автоматично потрапляють
# до панелі адміністратора
admin.site.register(User)
admin.site.register(Role)
admin.site.register(Access)
