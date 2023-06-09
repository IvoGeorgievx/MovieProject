import re

from marshmallow import ValidationError

from models import User, Hall


class UserValidator:
    @staticmethod
    def name_validator(value):
        for ch in value:
            if not ch.isalpha():
                raise ValidationError("Name must contain only alphabetic characters")

    @staticmethod
    def unique_username_validator(value):
        if User.query.filter_by(username=value).first():
            raise ValidationError("Username already exists")

    @staticmethod
    def username_validator(value):
        pattern = re.compile(r'[!@#$%^&*(),.?":{}|<>]')
        match = pattern.search(value)
        if match:
            raise ValidationError("Username can't contain special characters")

    @staticmethod
    def email_validator(value):
        pattern = re.compile(r"^[a-zA-Z0-9_.]{3,}@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
        match = pattern.search(value)
        if not match:
            raise ValidationError("Invalid email address")

    @staticmethod
    def unique_email_validator(value):
        if User.query.filter_by(email=value).first():
            raise ValidationError("Email already exists.")


class MovieValidator:
    @staticmethod
    def ticket_price_validator(value):
        if value <= 0:
            raise ValidationError("Ticket price must be higher than 0.")

    @staticmethod
    def rating_validator(value):
        if not 0 <= value <= 10:
            raise ValidationError("Movie ratings must be between 0 and 10 inclusive")


class HallValidator:
    @staticmethod
    def hall_id_validator(value):
        hall = Hall.query.filter_by(id=value).first()
        if not hall:
            raise ValidationError("Hall with that ID does not exist.")
