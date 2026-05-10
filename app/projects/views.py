from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Project
from .serializers import ProjectSerializer
from drf_spectacular.utils import extend_schema


# ========== GET /api/management/projects/ & POST /api/management/projects/ ==========
class ProjectListView(APIView):
    """
    List all Projects or Create a new Project
    """

    @extend_schema(tags=['Projects'], description='Get all Projects')
    def get(self, request):
        """GET - Retrieve all Projects"""
        projects = Project.objects.all().order_by('-created_at')
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    @extend_schema(tags=['Projects'], description='Create a new Project')
    def post(self, request):
        """POST - Create a new Project"""
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ========== GET /api/management/projects/{id}/, PUT, PATCH, DELETE ==========
class ProjectDetailView(APIView):
    """
    Retrieve, Update, or Delete a specific Project
    """

    @extend_schema(tags=['Projects'], description='Get a specific Project')
    def get(self, request, pk):
        """GET - Retrieve a specific Project by ID"""
        try:
            project = Project.objects.get(pk=pk)
            serializer = ProjectSerializer(project)
            return Response(serializer.data)
        except Project.DoesNotExist:
            return Response(
                {'error': 'Project not found'},
                status=status.HTTP_404_NOT_FOUND
            )

    @extend_schema(tags=['Projects'], description='Update entire Project')
    def put(self, request, pk):
        """PUT - Update entire Project (all fields required)"""
        try:
            project = Project.objects.get(pk=pk)
            serializer = ProjectSerializer(project, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Project.DoesNotExist:
            return Response(
                {'error': 'Project not found'},
                status=status.HTTP_404_NOT_FOUND
            )

    @extend_schema(tags=['Projects'], description='Partially update Project')
    def patch(self, request, pk):
        """PATCH - Partially update Project (only provided fields)"""
        try:
            project = Project.objects.get(pk=pk)
            serializer = ProjectSerializer(project, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Project.DoesNotExist:
            return Response(
                {'error': 'Project not found'},
                status=status.HTTP_404_NOT_FOUND
            )

    @extend_schema(tags=['Projects'], description='Delete a Project')
    def delete(self, request, pk):
        """DELETE - Delete a specific Project"""
        try:
            project = Project.objects.get(pk=pk)
            project.delete()
            return Response(
                {'message': 'Project deleted successfully'},
                status=status.HTTP_204_NO_CONTENT
            )
        except Project.DoesNotExist:
            return Response(
                {'error': 'Project not found'},
                status=status.HTTP_404_NOT_FOUND
            )
