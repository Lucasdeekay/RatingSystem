from django.urls import path

from MySite.views import DashboardView, LoginView, RegisterView, ForgotPasswordView, ChangePasswordView, LogoutView, \
    RankingView

app_name = "MySite"

urlpatterns = [
    path('', LoginView.as_view(), name="login"),
    path('register', RegisterView.as_view(), name="register"),
    path('logout', LogoutView.as_view(), name="logout"),
    path('forgot_password', ForgotPasswordView.as_view(), name="forgot_password"),
    path('forgot_password/change_password/<str:username>', ChangePasswordView.as_view(), name="change_password"),
    path('dashboard', DashboardView.as_view(), name="dashboard"),
    path('ranking', RankingView.as_view(), name="ranking"),
]