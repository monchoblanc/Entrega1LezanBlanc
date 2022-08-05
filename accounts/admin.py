from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin #para poder manejar los perfiles desde admin
from django.contrib.auth.models import User
from .models import Perfil

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class PerfilInline(admin.StackedInline):
    model = Perfil
    can_delete = False
    verbose_name_plural = 'perfil'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (PerfilInline,)

#regitro mi modelo Perfil. no hace falta si ya hago todo lo de abajo??
admin.site.register(Perfil)
# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)