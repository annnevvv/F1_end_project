from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [

    path('', views.goToMemberRegister, name='go_to_register_or_login'),
    path('signup', views.signUp, name='sign_up'),
    path('confirm-memeber-account-created', views.memberRegisterConfirmation,
         name='confirm-memeber-account-created'),

    path('password-change-done', auth_views.PasswordChangeDoneView.as_view(
        template_name='password-change-done.html')),
    path('password-change', auth_views.PasswordChangeView.as_view(
        template_name='password-change.html')),
    path('password-reset-done', auth_views.PasswordResetDoneView.as_view(
        template_name='password-reset-done.html')),
    path('password-reset', auth_views.PasswordResetView.as_view(
        template_name='password-reset.html')),

    path('dashboard', views.memberdashboard, name='member_dashboard'),

]
