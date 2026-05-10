from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import KPI
from .serializers import KPISerializer
from drf_spectacular.utils import extend_schema


# ========== GET /api/management/kpis/ & POST /api/management/kpis/ ==========
class KPIListView(APIView):
    """
    List all KPIs or Create a new KPI
    """

    @extend_schema(tags=['KPIs'], description='Get all KPIs')
    def get(self, request):
        """GET - Retrieve all KPIs"""
        kpis = KPI.objects.all()
        serializer = KPISerializer(kpis, many=True)
        return Response(serializer.data)

    @extend_schema(tags=['KPIs'], description='Create a new KPI')
    def post(self, request):
        """POST - Create a new KPI"""
        serializer = KPISerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ========== GET /api/management/kpis/{id}/, PUT, PATCH, DELETE ==========
class KPIDetailView(APIView):
    """
    Retrieve, Update, or Delete a specific KPI
    """

    @extend_schema(tags=['KPIs'], description='Get a specific KPI')
    def get(self, request, pk):
        """GET - Retrieve a specific KPI by ID"""
        try:
            kpi = KPI.objects.get(pk=pk)
            serializer = KPISerializer(kpi)
            return Response(serializer.data)
        except KPI.DoesNotExist:
            return Response(
                {'error': 'KPI not found'},
                status=status.HTTP_404_NOT_FOUND
            )

    @extend_schema(tags=['KPIs'], description='Update entire KPI')
    def put(self, request, pk):
        """PUT - Update entire KPI (all fields required)"""
        try:
            kpi = KPI.objects.get(pk=pk)
            serializer = KPISerializer(kpi, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except KPI.DoesNotExist:
            return Response(
                {'error': 'KPI not found'},
                status=status.HTTP_404_NOT_FOUND
            )

    @extend_schema(tags=['KPIs'], description='Partially update KPI')
    def patch(self, request, pk):
        """PATCH - Partially update KPI (only provided fields)"""
        try:
            kpi = KPI.objects.get(pk=pk)
            serializer = KPISerializer(kpi, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except KPI.DoesNotExist:
            return Response(
                {'error': 'KPI not found'},
                status=status.HTTP_404_NOT_FOUND
            )

    @extend_schema(tags=['KPIs'], description='Delete a KPI')
    def delete(self, request, pk):
        """DELETE - Delete a specific KPI"""
        try:
            kpi = KPI.objects.get(pk=pk)
            kpi.delete()
            return Response(
                {'message': 'KPI deleted successfully'},
                status=status.HTTP_204_NO_CONTENT
            )
        except KPI.DoesNotExist:
            return Response(
                {'error': 'KPI not found'},
                status=status.HTTP_404_NOT_FOUND
            )
