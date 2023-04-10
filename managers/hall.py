from werkzeug.exceptions import BadRequest

from db import db
from models import Hall, HallAvailability


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
    def check_hall_availability(start_time, end_time, hall_id):
        current_movies = HallAvailability.query.filter(
            HallAvailability.start_time <= end_time,
            HallAvailability.end_time >= start_time,
            HallAvailability.hall_id == hall_id
        ).all()
        if current_movies:
            raise BadRequest("Hall is occupied during that time.Set another timeframe or choose other hall.")

    @staticmethod
    def check_hall_capacity(hall_id):
        hall = Hall.query.filter_by(id=hall_id).first()
        if hall.capacity > 0:
            hall.capacity -= 1
            # TODO: Finish logic about this, make movies screen at exact time,
            #  then check capacity, when movie ends, restore default capacity

    @staticmethod
    def set_hall_occupancy(start_time, end_time, hall_id):
        hall = Hall.query.filter_by(id=hall_id).first()
        occupancy = HallAvailability(start_time=start_time,
                                     end_time=end_time,
                                     hall=hall)
        db.session.add(occupancy)
        db.session.commit()
        return occupancy
