from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from authservice.forms import LoginForm, UserRegistrationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from authservice.models import User

# Create your views here.

def home(request):
    return render(request, 'authservice/home.html')


def register(request):
    if request.user:
        print("Got user in session: ", request.user)
        request.session.flush()

    form = UserRegistrationForm()
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.pop("email")
            password = form.cleaned_data.pop("password")

            existing_user = User.objects.filter(email=email).first()
            if existing_user:
                form.add_error("email", "Email already exists.")
                return render(request, 'authservice/register.html', {"form": form})
            
            existing_user = User.objects.filter(phone_number=form.cleaned_data.get("phone_number")).first()
            if existing_user:
                form.add_error("phone_number", "phone number already exists.")
                return render(request, 'authservice/register.html', {"form": form})
            
            user = User.objects.create_user(email=email, password=password,**form.cleaned_data)
            messages.success(request, "Registration successful.")
            return HttpResponseRedirect(reverse("authservice:home"))

    return render(request, 'authservice/register.html', {"form": form})

def user_login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(request,email=email, password=password)
 
            if not user:    
                messages.error(request, "Invalid credentials.")
                return HttpResponseRedirect(reverse("authservice:user_login"))

            login(request,user)
            messages.success(request, "Login successful.")
            return HttpResponseRedirect(reverse("authservice:home"))

    return render(request, 'authservice/login.html', {"form": form})