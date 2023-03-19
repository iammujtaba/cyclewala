from django import forms
from utils.constants import INDIAN_STATE_CHOICES,ALL_COUNTRY_CHOICES, PHONE_NUMBER_COUNTRY_CODE
from utils.validators import validate_constant_choices, validate_phone_number
from rest_framework.exceptions import ValidationError

class AddNewAddressForm(forms.Form):
    flat = forms.CharField(max_length=50)
    street_address = forms.CharField(max_length=255)
    near_by_landmark = forms.CharField(max_length=255, required=False,label="Landmark")
    city = forms.CharField(max_length=50)
    state = forms.ChoiceField(choices=INDIAN_STATE_CHOICES)
    country = forms.ChoiceField(choices=ALL_COUNTRY_CHOICES)
    postal_code = forms.CharField(max_length=20,label="Pincode")
    email = forms.EmailField(required=False)
    phone_number = forms.CharField(max_length=10,min_length=10)
    country_code = forms.ChoiceField(choices=PHONE_NUMBER_COUNTRY_CODE,initial="+91")
    is_default_address = forms.BooleanField(required=False,label="Make default address")

    def clean(self):
        super(AddNewAddressForm,self).clean()
        street_address = self.cleaned_data.get("street_address")
        city = self.cleaned_data.get("city")
        state = self.cleaned_data.get("state")
        country = self.cleaned_data.get("country")
        postal_code = self.cleaned_data.get("postal_code")
        country_code = self.cleaned_data.pop("country_code",'')
        phone_number = self.cleaned_data.get("phone_number")
        email = self.cleaned_data.get("email")

        try:
            if phone_number:
                if phone_number.isdigit() is False:
                    raise ValidationError("Phone number input should contain only digits")
                phone_number = f"({country_code}){phone_number}"
                validate_phone_number(phone_number)  # Currently Indian numbers are allowed.
                self.cleaned_data["phone_number"] = phone_number
        except Exception as e:
            self._errors['phone_number'] = self.error_class([e.args[0]])

        try:
            validate_constant_choices(state,INDIAN_STATE_CHOICES)
        except Exception as e:
            self.add_error("state",e)
        try:
            validate_constant_choices(country,ALL_COUNTRY_CHOICES)
        except Exception as e:
            self.add_error("country",e)

        if email:
            email_suffix = email.split("@")[1]
            if email_suffix not in ["gmail.com","yahoo.com","hotmail.com","outlook.com"]:
                self._errors['email'] = self.error_class(['Only gmail, yahoo, hotmail and outlook emails are allowed.'])
        
        try:
            int(postal_code)
        except ValueError:
            self.add_error("postal_code","pincode should be number")


