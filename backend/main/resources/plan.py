from flask import request
from flask_restful import Resource

PLANES = {
    1: {'Primer Tratamiento': 'Fisioterapia', 'Segundo Tratamiento': 'Logopedia'},
    2: {'Primer Tratamiento': 'Masaje', 'Segundo Tratamiento': 'Caminata'}
}

class Plan(Resource):
    def get(self, id):
        if int(id) in PLANES:
            return PLANES[int(id)], 200
        return 'El plan no existe'
    
    def put(self, id):
        if int(id) in PLANES:
            data = request.get_json()
            plan = PLANES[int(id)]
            plan.update(data)
            return 'Plan actualizado con éxito', 200
        return 'El Plan no existe', 404

    def delete(self, id):
        if int(id) in PLANES:
            del PLANES[int(id)]
            return 'Plan eliminado con éxito', 200
        return 'El Plan no exixte', 404

class Planes(Resource):
    def get(self):
        return PLANES, 200
    
    def post(self):
        plan = request.get_json()
        id = int(max(PLANES.keys())) + 1
        PLANES[id] = plan
        return PLANES[id], 201
    
    