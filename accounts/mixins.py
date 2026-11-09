from functools import wraps
from django.contrib.auth.mixins import AccessMixin
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages


class RoleRequiredMixin(AccessMixin):
    """
    CBV mixin that enforces user roles.
    allowed_roles: list or tuple of role strings e.g. ['SUPER_ADMIN', 'SCHOOL_ADMIN']
    """
    allowed_roles = []

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()

        if request.user.is_superuser or getattr(request.user, 'role', None) == 'SUPER_ADMIN':
            return super().dispatch(request, *args, **kwargs)

        if self.allowed_roles and getattr(request.user, 'role', None) not in self.allowed_roles:
            raise PermissionDenied("You do not have permission to access this resource.")

        return super().dispatch(request, *args, **kwargs)


def role_required(*roles):
    """
    Decorator for views that checks whether a user has one of the specified roles.
    Superusers and SUPER_ADMIN users bypass all checks.
    """
    def decorator(view_func):
        @login_required
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_superuser or getattr(request.user, 'role', None) == 'SUPER_ADMIN':
                return view_func(request, *args, **kwargs)

            if getattr(request.user, 'role', None) not in roles:
                raise PermissionDenied("You do not have permission to access this resource.")

            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator


class SchoolScopedMixin:
    """
    Filters querysets by request.user.school for multi-tenancy.
    Super Admins and superusers can see all objects.
    """
    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user
        if not user.is_authenticated:
            return qs.none()

        if getattr(user, 'is_super_admin', False) or user.is_superuser:
            return qs

        if hasattr(user, 'school') and user.school:
            return qs.filter(school=user.school)

        return qs.none()
