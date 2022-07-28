from django.contrib import admin
from igsManager.models import Employee, Departament


# Register your models here.

class DepartamentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ['name']
    list_per_page = 20


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'departament')
    list_display_links = ('id', 'name', 'email', 'departament')
    search_fields = ['name', 'email']
    list_per_page = 20


admin.site.register(Departament, DepartamentAdmin)
admin.site.register(Employee, EmployeeAdmin)