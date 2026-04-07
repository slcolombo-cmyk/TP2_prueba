from flask import request
from flask_restful import Resource

class RegisterResource(Resource):
    def post(self):
        return {"mensaje": "Ruta de registro en construcción"}, 200