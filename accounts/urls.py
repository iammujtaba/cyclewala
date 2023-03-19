from django.urls import path
from accounts.views import my_account,add_new_address

app_name = "accounts"

urlpatterns = [
    path('myaccount/', my_account, name='myaccount'),
    path('addresses/add/', add_new_address, name='add_address'),
]
