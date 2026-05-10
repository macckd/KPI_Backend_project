
from django.db import models
from app.projects.models import Project

class KPI(models.Model):
    STATUS_CHOICES = [
        ('ON_TRACK', 'ON_TRACK'),
        ('AT_RISK', 'AT_RISK'),
        ('OFF_TRACK', 'OFF_TRACK')
    ]

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='kpis')
    name = models.CharField(max_length=255)
    target = models.FloatField()
    actual = models.FloatField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
