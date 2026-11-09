from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('', views.StudentListView.as_view(), name='list'),
    path('add/', views.StudentCreateView.as_view(), name='add'),
    path('<int:pk>/', views.StudentDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', views.StudentUpdateView.as_view(), name='edit'),
    path('import/', views.StudentImportView.as_view(), name='import'),
    path('classes/', views.StudentClassesView.as_view(), name='classes'),
    path('dorms/', views.StudentDormsView.as_view(), name='dorms'),
]
