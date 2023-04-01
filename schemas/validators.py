from marshmallow import ValidationError


def name_validator(value):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError("Name must contain only alphabetic characters")


def rating_validator(value):
    if not 0 <= value <= 5:
        raise ValidationError("Movie rating must be between 0 and 5 inclusive")
