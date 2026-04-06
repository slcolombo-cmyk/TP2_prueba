from flask import request
from flask_restful import Resource

PLANES = {
    1: {'Primer Tratamiento:': '.....', 'Segundo Tratamiento': '.....'},
    2: {'Primer Tratamiento:': '.....', 'Segundo Tratamiento': '.....'}
}

class Plan(Resource):
    def get(self, id):
        if int(id) in PLANES:
            return PLANES[int(id)], 200
        return 'El plan no existe'

class Planes(Resource):
    def get(self):
        return PLANES, 200
    
    def post(self):
        plan = request.get_json()
        id = int(max(PLANES.keys())) + 1
        PLANES[id] = plan
        return PLANES[id], 201