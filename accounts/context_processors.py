def user_roles(request):
    """
    Exposes user role and tenancy data to templates.
    """
    user = request.user
    if not user.is_authenticated:
        return {
            'current_school': None,
            'is_super_admin': False,
            'is_school_admin': False,
            'is_teacher': False,
            'is_bursar': False,
            'user_role_label': 'Guest',
        }

    school = getattr(user, 'school', None)
    return {
        'current_school': school,
        'is_super_admin': getattr(user, 'is_super_admin', False) or user.is_superuser,
        'is_school_admin': getattr(user, 'is_school_admin', False),
        'is_teacher': getattr(user, 'is_teacher', False),
        'is_bursar': getattr(user, 'is_bursar', False),
        'user_role_label': user.get_role_display() if hasattr(user, 'get_role_display') else 'User',
    }
