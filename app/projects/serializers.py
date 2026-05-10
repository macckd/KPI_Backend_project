from rest_framework import serializers
from .models import Project
from app.kpis.serializers import KPISerializer


class ProjectSerializer(serializers.ModelSerializer):
    kpis = KPISerializer(many=True, read_only=True)  # Add this line

    class Meta:
        model = Project
        fields = '__all__'
