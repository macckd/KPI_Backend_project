from django.urls import path, include

urlpatterns = [
    path('kpis/', include('app.kpis.urls')),
    path('projects/', include('app.projects.urls')),
]