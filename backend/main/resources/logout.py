from flask import request
from flask_restful import Resource

class LogoutResource(Resource):
    def post(self):
        return {"mensaje": "Ruta de logout en construcción"}, 200