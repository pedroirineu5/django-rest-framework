from django.contrib import admin

from publisher.models import Publisher


@admin.register(Publisher)
class AdminPublisher(admin.ModelAdmin):
    list_display = ('id', 'name')