from django.urls import path
from authservice.views import user_login,verify_otp
urlpatterns = [
    path('login/', user_login, name='login'),
    path('verify-otp/', verify_otp, name='verify_otp'),
]
