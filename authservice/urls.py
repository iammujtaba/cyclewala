from django.urls import path
from authservice.views import register,home,user_login

app_name = "authservice"

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='user_login'),

    path('home/', home, name='home'),
]
