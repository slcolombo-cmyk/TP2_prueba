from flask import request
from flask_restful import Resource

class LoginResource(Resource):
    def post(self):
        return {"mensaje": "Ruta de login en construcción"}, 200