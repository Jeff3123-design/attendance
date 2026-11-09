"""
URL configuration for attendance_system project.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import api_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth routes at root as specified (/login/, /logout/, etc.)
    path('', include('accounts.urls')),

    # Dashboard at root
    path('', include('dashboard.urls')),

    # Core system apps
    path('schools/', include('schools.urls')),
    path('students/', include('students.urls')),
    path('staff/', include('staff.urls')),
    path('devices/', include('devices.urls')),
    path('attendance/', include('attendance.urls')),
    path('reports/', include('reports.urls')),
    path('notifications/', include('notifications.urls')),
    path('settings/', include('accounts.settings_urls')),
    path('audit/', include('audit.urls')),

    # Placeholder API endpoints
    path('api/adms/cdata', api_views.adms_cdata, name='api_adms_cdata'),
    path('api/adms/getrequest', api_views.adms_getrequest, name='api_adms_getrequest'),
    path('api/attendance/', api_views.api_attendance, name='api_attendance'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
