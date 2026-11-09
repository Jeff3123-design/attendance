from django.urls import path
from . import views

app_name = 'reports'

urlpatterns = [
    path('', views.ReportIndexView.as_view(), name='index'),
    path('daily/', views.ReportDailyView.as_view(), name='daily'),
    path('weekly/', views.ReportWeeklyView.as_view(), name='weekly'),
    path('termly/', views.ReportTermlyView.as_view(), name='termly'),
    path('student/<int:pk>/', views.ReportStudentView.as_view(), name='student'),
    path('class/<int:pk>/', views.ReportClassView.as_view(), name='class'),
    path('export/', views.ReportExportView.as_view(), name='export'),
]
