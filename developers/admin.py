from django.contrib import admin

from developers.models import Developers


@admin.register(Developers)
class AdminDevelopers(admin.ModelAdmin):
    list_display = ('id','name','age','birthday','nationality')
    