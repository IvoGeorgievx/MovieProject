from db import db
from models import Hall


class HallManager:

    @staticmethod
    def create_hall(data):
        hall = Hall(**data)
        db.session.add(hall)
        db.session.commit()
        return hall

    @staticmethod
    def delete_hall(data):
        pass

    @staticmethod
    def check_hall_capacity(hall_id):
        hall = Hall.query.filter_by(id=hall_id).first()
        if hall.capacity > 0:
            hall.capacity -= 1
            # TODO: Finish logic about this, make movies screen at exact time,
            #  then check capacity, when movie ends, restore default capacity
