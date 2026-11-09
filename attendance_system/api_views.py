"""
Placeholder API endpoints for biometric terminal communication (ZKTeco ADMS) and attendance integration.
"""

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def adms_cdata(request):
    """ZKTeco ADMS/PUSH data receiver stub."""
    return JsonResponse({"status": "not implemented", "endpoint": "adms/cdata"})


@csrf_exempt
def adms_getrequest(request):
    """ZKTeco ADMS command polling stub."""
    return JsonResponse({"status": "not implemented", "endpoint": "adms/getrequest"})


@csrf_exempt
def api_attendance(request):
    """Attendance API stub."""
    return JsonResponse({"status": "not implemented", "endpoint": "api/attendance"})
