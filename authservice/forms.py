from django import forms
from rest_framework.exceptions import ValidationError
from utils.constants import PHONE_NUMBER_COUNTRY_CODE
from utils.validators import validate_phone_number


class UserRegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField(required=False)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    phone_number = forms.CharField(max_length=10,min_length=10)
    country_code = forms.CharField(max_length=8,min_length=1,widget=forms.Select(choices=PHONE_NUMBER_COUNTRY_CODE))


    def clean(self):
        super(UserRegistrationForm,self).clean()

        country_code = self.cleaned_data.pop("country_code",'')
        phone_number = self.cleaned_data.get("phone_number")
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")
    
        try:
            if phone_number:
                if phone_number.isdigit() is False:
                    raise ValidationError("Phone number input should contain only digits")
                phone_number = f"({country_code}){phone_number}"
                validate_phone_number(phone_number)  # Currently Indian numbers are allowed.
                self.cleaned_data["phone_number"] = phone_number
        except Exception as e:
            self._errors['phone_number'] = self.error_class([e.args[0]])

        if password != confirm_password:
            self._errors['password'] = self.error_class(['password and confirm password should be same.'])
            self._errors['confirm_password'] = self.error_class(['password and confirm password should be same.'])


        if email:
            email_suffix = email.split("@")[1]
            if email_suffix not in ["gmail.com","yahoo.com","hotmail.com","outlook.com"]:
                self._errors['email'] = self.error_class(['Only gmail, yahoo, hotmail and outlook emails are allowed.'])
        
        self.cleaned_data.pop("confirm_password",None)


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def clean(self):
        super(LoginForm,self).clean()
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        if email:
            email_suffix = email.split("@")[1]
            if email_suffix not in ["gmail.com","yahoo.com","hotmail.com","outlook.com"]:
                self._errors['email'] = self.error_class(['only gmail, yahoo, hotmail and outlook emails are allowed.'])
