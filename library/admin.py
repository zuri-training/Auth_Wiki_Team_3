from django.contrib import admin
from .models import AuthCode, Comment, Notification

# Register your models here.
admin.site.register(AuthCode)
admin.site.register(Comment)
admin.site.register(Notification)
