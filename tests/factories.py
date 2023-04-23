import factory

from db import db
from models import User, UserRole


class BaseFactory(factory.Factory):
    @classmethod
    def create(cls, **kwargs):
        object = super().create(**kwargs)
        db.session.add(object)
        db.session.flush()
        return object


class UserFactory(BaseFactory):
    class Meta:
        model = User

    id = factory.Sequence(lambda n: n)
    username = factory.Faker("user_name")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    email = factory.Faker("email")
    password = factory.Faker("password")
    role = UserRole.regular
    stripe_account = factory.Faker("uuid4")


# class MovieFactory(BaseFactory):
#     class Meta:
#         model = Movie
#
#     id = factory.Sequence(lambda n: n)
#     name = factory.Faker("name")
#     rating = factory.Faker("random_int", min=1, max=10)
#     description = factory.Faker("sentence")
#
#     ticket_count = factory.Faker("random_int", min=1, max=100)
#     ticket_price = factory.Faker("pyfloat", positive=True, min_value=1, max_value=100)
#     start_time = factory.Faker("date_time_between", start_date="+1d", end_date="+30d")
#     end_time = factory.LazyAttribute(lambda obj: obj.start_time + timedelta(hours=2))

# Tried to implement MovieFactory, but it kept raising TypeErrors


def normal_test_movie_data(hall):
    return {
        "name": "Test Movie",
        "rating": 5.0,
        "description": "one of the best movies",
        "hall_id": hall.id,
        "ticket_price": 35.65,
        "start_time": "2023-04-17T21:31:00.000000",
        "end_time": "2023-04-17T22:30:00.000000",
    }
