from django.urls import path,re_path
from . import views
from django.contrib.auth.views import (
     LoginView,
     LogoutView,
     PasswordResetView,
     PasswordResetDoneView,
     PasswordResetConfirmView,
     PasswordResetCompleteView,
)
app_name="accounts"

urlpatterns=[
    path('login/',LoginView.as_view(template_name="accounts/login.html"),name="login"),
    path('logout/',LogoutView.as_view(template_name="accounts/logout.html"),name="logout"),
    path('register/',views.register,name="register"),
    path('profile/',views.profile,name="profile"),
    path('profile/<int:pk>/',views.profile,name="profile_with_pk"),
    path('profile/edit/',views.edit_profile,name="edit_profile"),
    path('change-password/',views.change_password,name="change_password"),# PasswordChangeForm
    path('password-reset/',PasswordResetView.as_view(template_name='registration/password_reset.html'),
    name="password_reset"),
    path('password-reset/done/',PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),
    name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>/',PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),
    name="password_reset_confirm"),
    path('password-reset-complete/',PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
    name="password_reset_complete"),


]
