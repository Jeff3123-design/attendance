from django.urls import path
from . import views

app_name = 'devices'

urlpatterns = [
    path('', views.DeviceListView.as_view(), name='list'),
    path('add/', views.DeviceCreateView.as_view(), name='add'),
    path('<int:pk>/', views.DeviceDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', views.DeviceUpdateView.as_view(), name='edit'),
    path('<int:pk>/enroll/', views.DeviceEnrollView.as_view(), name='enroll'),
    path('sync-status/', views.DeviceSyncStatusView.as_view(), name='sync_status'),
]
