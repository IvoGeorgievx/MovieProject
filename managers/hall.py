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
    def check_hall_availability(start_time, end_time, hall_id):
        if end_time <= start_time:
            raise BadRequest("End time must be greater than start time")
        current_movies = HallAvailability.query.filter(
            HallAvailability.start_time <= end_time,
            HallAvailability.end_time >= start_time,
            HallAvailability.hall_id == hall_id,
        ).all()
        if current_movies:
            raise BadRequest(
                "Hall is occupied during that time.Set another timeframe or choose other hall."
            )

    @staticmethod
    def set_hall_occupancy(start_time, end_time, movie_id, hall_id):
        hall = Hall.query.filter_by(id=hall_id).first()
        occupancy = HallAvailability(
            start_time=start_time, end_time=end_time, movie_id=movie_id, hall=hall
        )
        db.session.add(occupancy)
        db.session.commit()
        return occupancy

    @staticmethod
    def remove_hall_occupancy(movie_id):
        hall = HallAvailability.query.filter_by(movie_id=movie_id).first()
        db.session.delete(hall)
        db.session.commit()
