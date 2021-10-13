from django.contrib import admin
from django.db.models.fields import IPAddressField
from .models import Task

admin.site.register(Task)
