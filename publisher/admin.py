from django.contrib import admin


@admin.register()
class AdminPublisher(admin.ModelAdmin):
    list_display = ('id', 'name')