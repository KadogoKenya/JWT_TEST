from django.urls import path
from users.views import RegistrationAPIView

app_name = 'users'
urlpatterns = [
    path('users/', RegistrationAPIView.as_view()),
]