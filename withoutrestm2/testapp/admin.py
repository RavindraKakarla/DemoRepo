from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "rollno", "marks", "gf", "bf"]



admin.site.register(Student, StudentAdmin)