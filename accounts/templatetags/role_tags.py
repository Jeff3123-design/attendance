from django import template

register = template.Library()


@register.filter(name='has_role')
def has_role(user, role_names):
    """
    Check if a user has any of the comma-separated roles.
    Superusers and SUPER_ADMIN have all roles.
    Usage: {% if request.user|has_role:"SUPER_ADMIN,SCHOOL_ADMIN" %}
    """
    if not user or not user.is_authenticated:
        return False
    if user.is_superuser or getattr(user, 'role', '') == 'SUPER_ADMIN':
        return True

    allowed = [r.strip() for r in role_names.split(',')]
    return getattr(user, 'role', '') in allowed


@register.filter(name='is_active_path')
def is_active_path(request, path_prefix):
    """
    Returns 'active' if the current request path starts with path_prefix.
    """
    if not request:
        return ''
    if path_prefix == '/' and request.path == '/':
        return 'active'
    if path_prefix != '/' and request.path.startswith(path_prefix):
        return 'active'
    return ''
