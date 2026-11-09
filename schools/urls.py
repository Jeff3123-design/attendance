from django.urls import path
from . import views

app_name = 'schools'

urlpatterns = [
    path('', views.SchoolListView.as_view(), name='list'),
    path('add/', views.SchoolCreateView.as_view(), name='add'),
    path('<int:pk>/', views.SchoolDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', views.SchoolUpdateView.as_view(), name='edit'),
]
