from django.contrib import admin
from Sitio.models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class PersonalizadoUserAdmin(UserAdmin):
    fieldsets = ()
    add_fieldsets = (
        (None,{
            'fields':('email,password1,password2')
        })
    )

    list_display = ('email','is_active','is_staff')
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(Usuario,PersonalizadoUserAdmin)
admin.site.register(Rescatado)