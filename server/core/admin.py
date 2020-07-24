from django.contrib import admin
from .models import *


@admin.register(Tree)
class TreeAdmin(admin.ModelAdmin):
    pass
