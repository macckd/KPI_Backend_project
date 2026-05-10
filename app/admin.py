from django.contrib import admin
from app.kpis.models import KPI
from app.projects.models import Project

admin.site.register(KPI)
admin.site.register(Project)