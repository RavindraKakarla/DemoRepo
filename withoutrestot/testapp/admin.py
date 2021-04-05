# from django.contrib import admin
# from withoutrestot.testapp.models import Employee
#
# class EmployeeAdmin(admin.ModelAdmin):
#     list_display = ["eno", "ename", "esal", "eaddr"]
#
# admin.site.register(Employee, EmployeeAdmin)
from django.contrib import admin
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["id", "eno", "ename", "esal", "eaddr"]

admin.site.register(Employee, EmployeeAdmin)