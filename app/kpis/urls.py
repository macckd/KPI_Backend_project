from django.urls import path
from .views import KPIListView, KPIDetailView

urlpatterns = [
    path('', KPIListView.as_view(), name='kpi-list'),
    path('<int:pk>/', KPIDetailView.as_view(), name='kpi-detail'),
]
