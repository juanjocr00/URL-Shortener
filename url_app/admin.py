from django.contrib import admin

from .models import shorterURL

@admin.register(shorterURL)
# Register your models here.
class shorterURLAdmin(admin.ModelAdmin):
    list_display = ['original_url', 'shorter_url', 'visit_count', 'private', 'username']