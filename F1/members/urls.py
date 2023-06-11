from django.urls import path
from django.contrib.auth import views as auth_views

from .views import goToMemberRegister, signUp, memberRegisterConfirmation, memberDashboard

urlpatterns = [

    path('', goToMemberRegister, name='go_to_register_or_login'),
    path('signup', signUp, name='sign_up'),
    path('confirm-member-account-created', memberRegisterConfirmation,
         name='confirm-member-account-created'),

    path('password-change-done', auth_views.PasswordChangeDoneView.as_view(
        template_name='password-change-done.html')),
    path('password-change', auth_views.PasswordChangeView.as_view(
        template_name='password-change.html')),
    path('password-reset-done', auth_views.PasswordResetDoneView.as_view(
        template_name='password-reset-done.html')),
    path('password-reset', auth_views.PasswordResetView.as_view(
        template_name='password-reset.html')),

    path('dashboard', memberDashboard, name='member_dashboard'),

]
