from django.shortcuts import render
from accounts.forms import AddNewAddressForm
# Create your views here.


def my_account(request):
    return render(request, 'accounts/my_account.html')


def add_new_address(request):
    form = AddNewAddressForm()
    if request.method == "POST":
        form = AddNewAddressForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    return render(request, 'accounts/add_address.html',{"form":form})