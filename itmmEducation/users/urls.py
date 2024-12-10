from django.urls import path
from . import views
from django.contrib.auth.views import LoginView


class CustomLoginView(LoginView):
    template_name = 'users/login.html'

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
]