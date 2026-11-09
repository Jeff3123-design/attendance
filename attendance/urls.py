from django.urls import path
from . import views

app_name = 'attendance'

urlpatterns = [
    path('today/', views.TodayAttendanceView.as_view(), name='today'),
    path('logs/', views.AttendanceLogsView.as_view(), name='logs'),
    path('daily/', views.DailyAttendanceView.as_view(), name='daily'),
    path('by-class/', views.ByClassAttendanceView.as_view(), name='by_class'),
    path('by-dorm/', views.ByDormAttendanceView.as_view(), name='by_dorm'),
    path('late/', views.LateAttendanceView.as_view(), name='late'),
    path('absent/', views.AbsentAttendanceView.as_view(), name='absent'),
    path('manual-entry/', views.ManualEntryAttendanceView.as_view(), name='manual_entry'),
    path('rules/', views.AttendanceRulesView.as_view(), name='rules'),
]
