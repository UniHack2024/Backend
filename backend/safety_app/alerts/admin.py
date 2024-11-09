from django.contrib import admin
from .models import Category, Warning, CivicReport

# Register your models here.

admin.site.register(Category)
admin.site.register(Warning)
admin.site.register(CivicReport)

