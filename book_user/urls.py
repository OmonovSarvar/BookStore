from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, \
    PasswordResetCompleteView
from django.urls import path

from book_user.views import LoginView

urlpatterns = [
    path('api/login', LoginView.as_view()),
    path('password-reset', PasswordResetView.as_view(), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset-done', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset-complete', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
