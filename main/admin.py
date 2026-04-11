from django.contrib import admin
from main import models

admin.site.register(models.NUser)
admin.site.register(models.ChatMessage)