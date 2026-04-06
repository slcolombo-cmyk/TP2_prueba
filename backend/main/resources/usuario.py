from flask import request
from flask_restful import Resource

USUARIOS = {
    1: {'Nombre': 'Homero', 'Telefono': '9999-9999', 'Email': 'homero.gmail.com', 'DNI': '23453534'},
    2: {'Nombre': 'Bart', 'Telefono': '8888-8888', 'Email': 'barto.gmail.com', 'DNI': '129313232'}
}

FICHAS = {
    1: {'Tratamiento': '.....', 'Ejercicio': '.....' },
    2: {'Tratamiento': '.....', 'Ejercicio': '.....' }
}

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

class Ficha(Resource):
    def get(self, id):
        if int(id) in FICHAS:
            return FICHAS[int(id)], 200
        return 'La ficha no existe', 404

class Fichas(Resource):
    def get(self):
        return FICHAS, 200

    def post(self):
        ficha = request.get_json()
        id = int(max(FICHAS.keys())) + 1
        FICHAS[id] = ficha
        return FICHAS[id], 201

class Usuario(Resource):
    def get(self, id):
        if int(id) in USUARIOS:
            return USUARIOS[int(id)], 200
        return 'El usuario no existe', 404

    def put(self, id):
        if int(id) in USUARIOS:
            data = request.get_json()
            usuario = USUARIOS[int(id)]
            usuario.update(data)
            return 'Usuario actualizado con éxito', 200
        return 'El usuario no existe', 404

    def delete(self, id):
        if int(id) in USUARIOS:
            del USUARIOS[int(id)]
            return 'Usuario eliminado con éxito', 200
        return 'El usuario no exixte', 404

class Usuarios(Resource):
    def get(self):
        return USUARIOS, 200

    def post(self):
        usuario = request.get_json()
        id = int(max(USUARIOS.keys())) + 1
        USUARIOS[id] = usuario
        return USUARIOS[id], 201
