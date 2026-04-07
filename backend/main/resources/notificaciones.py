from flask import request
from flask_restful import Resource

class NotificacionesResource(Resource):
    def get(self):
        return {"mensaje": "Ruta de notificaciones en construcción"}, 200