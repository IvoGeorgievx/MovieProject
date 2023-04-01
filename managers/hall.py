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