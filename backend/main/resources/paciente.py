from flask import request
from flask_restful import Resource

PACIENTES = {
    1: {'nombre': 'Homero', 'telefono': '9999-9999', 'email': 'homero.gmail.com', 'dni': '23453534'},
    2: {'nombre': 'Bart', 'telefono': '8888-8888', 'email': 'barto.gmail.com', 'dni': '129313232'}
}

class Paciente(Resource):
    def get(self, id):
        if int(id) in PACIENTES:
            return PACIENTES[int(id)], 200
        return 'El animal no existe', 404

    def put(self, id):
        if int(id) in PACIENTES:
            data = request.get_json()
            paciente = PACIENTES[int(id)]
            paciente.update(data)
            return 'Animal actualizado con éxito', 200
        return 'El animal no existe', 404

    def delete(self, id):
        if int(id) in PACIENTES:
            del PACIENTES[int(id)]
            return 'Animal eliminado con éxito', 200
        return 'El animla no exixte', 404

class Pacientes(Resource):
    def get(self):
        return PACIENTES, 200

    def post(self):
        paciente = request.get_json()
        id = int(max(PACIENTES.keys())) + 1
        PACIENTES[id] = paciente
        return PACIENTES[id], 201
