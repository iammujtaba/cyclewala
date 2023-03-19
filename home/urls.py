from django.urls import path
from home.views import homepage

app_name = "home"

urlpatterns = [
    path('', homepage, name='homepage'),
    path('home/', homepage, name='homepage'),
]
