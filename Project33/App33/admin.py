from django.contrib import admin
from .models import *

# Register your models here.
# моделі, зареєстровані у даному файлі, автоматично потрапляють
# до панелі адміністратора
class UserModelAdmin(admin.ModelAdmin) :
    list_display = ('first_name','last_name','email','phone','birthdate' )


admin.site.register(User, UserModelAdmin)
admin.site.register(Role)
admin.site.register(Access)