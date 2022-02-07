from django import forms
from rest_framework.exceptions import ValidationError
from utils.constants import PHONE_NUMBER_COUNTRY_CODE


class LoginForm(forms.Form):
    email = forms.EmailField(label='',required=False,
                            widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    phone_number = forms.CharField(label = "", max_length=10,required=False,
                                    widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),min_length=8,required=False,label='')
    country_code = forms.CharField(label="",max_length=6,widget=forms.Select(choices=PHONE_NUMBER_COUNTRY_CODE),required=False)

    def clean(self):
        super(LoginForm,self).clean()
        phone_number = self.cleaned_data.get("phone_number")
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        country_code = self.cleaned_data.pop("country_code",'')
    
        try:
            if phone_number:
                if phone_number.isdigit() is False:
                    raise ValidationError("Phone number input should contain only digits")
                phone_number = f"({country_code}){phone_number}"
                # validate_phone_number(phone_number)  # Validate phone number logic will be added (Only for Indian numbers and basic checks for International numbers)
                self.cleaned_data["phone_number"] = phone_number
        except Exception as e:
            self._errors['phone_number'] = self.error_class([e.args[0]])

        if phone_number and (email or password):
            self._errors['phone_number'] = self.error_class([
                'Either phone number or email and password is required.'])
            self._errors['email'] = self.error_class([
                'Either phone number or email and password is required.'])
        if not phone_number and not email and not password:
            self._errors['phone_number'] = self.error_class([
                'Either phone number or email and password is required.'])
            self._errors['email'] = self.error_class([
                'Either phone number or email and password is required.'])

class VerifyOTP(forms.Form):
    otp = forms.CharField(label = "", max_length=6,required=False,
                                    widget=forms.TextInput(attrs={'placeholder': 'Enter your 6 digit OTP'}))
