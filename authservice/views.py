from django.shortcuts import render
from authservice.forms import LoginForm, VerifyOTP


def user_login(request):
    form = LoginForm()
    # Remaining logic will be added here.
    return render(request,'users/login.html',{'form':form})

def verify_otp(request):
    form = VerifyOTP()
    # Remaining logic will be added here.
    return render(request,'users/verify-otp.html',{'form':form})