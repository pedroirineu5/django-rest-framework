from django.contrib import admin

from platforms.models import Platforms


@admin.register(Platforms)
class PlatformsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')