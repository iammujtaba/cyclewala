import re

from rest_framework.exceptions import ValidationError

PHONE_REGEX_STR = "^[0-9 | ( | ) | + | - ]*$"
PHONE_REGEX = re.compile(PHONE_REGEX_STR)


def _soft_validate_phone_number(value):
    return bool(PHONE_REGEX.match(value)) if value else False

def validate_phone_number(value,soft_validate=False):
    if soft_validate:
        return _soft_validate_phone_number(value)

    if not value:
        return value

    if not 10 <= len(value) <= 18:
        raise ValidationError("Phone number length should between 7 to 15 digit")

    if "+" not in value or ")" not in value or "(" not in value:
        raise ValidationError("Phone number should be in (+XX)XXXXXXXXXX format")

    phone_number = value.split(")")[-1]
    if "+91" not in value:
        raise ValidationError("Currently only Indian numbers are allowed") #will remove this check later

    if len(phone_number) != 10:
        raise ValidationError("Indian phone number length should be equal to 10") #will remove this check later
    
    if "+91" not in value and len(phone_number) > 10:
        raise ValidationError("Phone number length should be less than equals to 10.")

    if "+91" in value and "(" not in value and ")" not in value:
        phone_number = value.split("+91") 

        if len(phone_number) < 10:
            raise ValidationError("Phone number length should be equal to 10")

    if not PHONE_REGEX.match(value):
        raise ValidationError('Incorrect phone number')    
    


def validate_constant_choices(value,choices): #format of choices is [(1,"one"),(2,"two")]
    if value not in [choice[0] for choice in choices]:
        raise ValidationError(f"{value} is not a valid choice")
