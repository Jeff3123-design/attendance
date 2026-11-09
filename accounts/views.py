from django.contrib.auth import views as auth_views
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View


class UserLoginView(auth_views.LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Sign In'
        return context


class UserLogoutView(View):
    """Handles both GET and POST logout requests cleanly."""
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('accounts:login')

    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect('accounts:login')


class UserPasswordChangeView(auth_views.PasswordChangeView):
    template_name = 'registration/password_change.html'
    success_url = reverse_lazy('accounts:password_change_done')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Change Password'
        return context


class UserPasswordChangeDoneView(auth_views.PasswordChangeDoneView):
    template_name = 'registration/password_change_done.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Password Changed'
        return context


class UserPasswordResetView(auth_views.PasswordResetView):
    template_name = 'registration/password_reset.html'
    email_template_name = 'registration/password_reset_email.html'
    success_url = reverse_lazy('accounts:password_reset_done')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Reset Password'
        return context


class UserPasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'registration/password_reset_done.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Password Reset Sent'
        return context
