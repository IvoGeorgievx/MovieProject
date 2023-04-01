from flask import request
from flask_restful import Resource

from managers.auth import auth
from managers.hall import HallManager
from models import UserRole
from schemas.request.hall import HallSchemaIn
from schemas.response.hall import HallSchemaOut
from utilities.decorators import validate_schema, permission_required


class Hall(Resource):
    @auth.login_required
    @permission_required(UserRole.admin)
    @validate_schema(HallSchemaIn)
    def post(self):
        data = request.get_json()
        hall = HallManager.create_hall(data)
        return HallSchemaOut().dump(hall)
