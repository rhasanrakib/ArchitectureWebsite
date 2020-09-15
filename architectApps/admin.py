from django.contrib import admin
from . models import Company_details, Academic, Professional
# Register your models here.
admin.site.register(Company_details)
admin.site.register(Academic)
admin.site.register(Professional)
