from django.contrib import admin
from .models import Talaba


@admin.register(Talaba)
class TalabaAmin(admin.ModelAdmin):
    list_display = ["name","age","contact_number"]