from django.contrib import admin
from .models import Doctor



@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'birthday', 'age', 'phone', 'degree', 'email')
    list_filter = ('degree',)
    search_fields = ('name', 'email')
