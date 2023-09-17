from django.urls import path, include
from .views import Login, Register, Logout
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path("accounts/login/", Login.as_view(), name="login"),
    path("accounts/logout/", Logout.as_view(), name="logout"),
    path("accounts/register/", Register.as_view(), name="register"),
    path("chat/", login_required(views.chatbot, login_url='/gpt/accounts/login/'), name='home')
]