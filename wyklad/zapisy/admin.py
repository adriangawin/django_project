from django.contrib import admin

# Register your models here.
from .models import Student, Wykladowca, Wyklad
admin.site.register(Wykladowca)
admin.site.register(Student)
admin.site.register(Wyklad)
