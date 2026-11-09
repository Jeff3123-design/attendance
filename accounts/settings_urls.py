from django.urls import path
from . import settings_views

app_name = 'settings'

urlpatterns = [
    path('profile/', settings_views.ProfileSettingsView.as_view(), name='profile'),
    path('school/', settings_views.SchoolSettingsView.as_view(), name='school'),
    path('users/', settings_views.UserManagementView.as_view(), name='users'),
    path('users/add/', settings_views.UserAddView.as_view(), name='users_add'),
    path('consent/', settings_views.ConsentPolicySettingsView.as_view(), name='consent'),
    path('backup/', settings_views.BackupSettingsView.as_view(), name='backup'),
]
