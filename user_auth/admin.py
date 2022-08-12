from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import OurUser
# from library.models import AuthCode


class OurUserAdmin(BaseUserAdmin):
  list_display = ('username', 'email', 'tos',
                  'date_joined', 'is_active', 'is_admin',)

  search_fields = ('username', 'email', 'date_joined',)

  readonly_fields = ('date_joined',)

  filter_horizontal = ()

  list_filter = ('last_login', 'is_active', 'is_admin',)

  fieldsets = ()

  add_fieldsets = (
      (None, {
          'classes': ('wide'),
          'fields': ('username', 'email', 'tos', 'password1', 'password2'),
      }),
  )

  ordering = ('username',)


# Register your models here.
admin.site.register(OurUser, OurUserAdmin)
