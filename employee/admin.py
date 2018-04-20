from django.contrib import admin
from .models import Employee, Department


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Employee Info', {'fields': ['name', 'email']}),
        ('Department', {'fields': ['department']}),
    ]

    list_display = ('name', 'email', 'department')
    list_display_links = ('name', 'department',)
    search_fields = ['name', 'department__name', ]


admin.site.register(Department)
