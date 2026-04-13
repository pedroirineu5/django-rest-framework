from django.contrib import admin

from reviews.models import Review

@admin.register(Review)
class reviewsAdmin(admin.ModelAdmin):
    list_display = ('id','game','grade')
