from django.urls import path
from django.contrib.auth import views as auth_views

from .views import go_to_member_register, signUp, member_register_confirmation, \
    member_dashboard, delete_member_account, SubPasswordChangeView, SubPasswordChangeDoneView

urlpatterns = [

    path('', go_to_member_register, name='go_to_register_or_login'),
    path('signup', signUp, name='sign_up'),
    path('confirm-member-account-created', member_register_confirmation,
         name='confirm-member-account-created'),
    path('delete-member-account', delete_member_account,
         name='delete_member_account'),

    path('password-change', SubPasswordChangeView.as_view(),
         name='password-change1'),
    path('password-change-done', SubPasswordChangeDoneView.as_view(),
         name='password-change-done.html'),
    path('password-reset-done', auth_views.PasswordResetDoneView.as_view(
        template_name='password-reset-done.html')),
    path('password-reset', auth_views.PasswordResetView.as_view(
        template_name='password-reset.html')),

    path('dashboard', member_dashboard, name='member_dashboard'),

]
