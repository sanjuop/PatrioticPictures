from django.contrib import admin
from userprofile.models import Department, Profile

# Register your models here.
admin.site.register(Profile)
admin.site.register(Department)