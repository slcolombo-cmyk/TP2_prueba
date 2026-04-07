from flask import request
from flask_restful import Resource

FICHAS = {
    1: {'Dia 1': 'Sentadillas y peso muerto', 'Dia 2': 'Press banca' },
    2: {'Dia 1': 'Mancuernas', 'Dia 2': 'Espalda' }
}

class Ficha(Resource):
    def get(self, id):
        if int(id) in FICHAS:
            return FICHAS[int(id)], 200
        return 'La ficha no existe', 404
    
    def put(self, id):
        if int(id) in FICHAS:
            data = request.get_json()
            ficha = FICHAS[int(id)]
            ficha.update(data)
            return 'Ficha actualizado con éxito', 200
        return 'El ficha no existe', 404

    def delete(self, id):
        if int(id) in FICHAS:
            del FICHAS[int(id)]
            return 'Ficha eliminado con éxito', 200
        return 'El Ficha no exixte', 404

class Fichas(Resource):
    def get(self):
        return FICHAS, 200

    def post(self):
        ficha = request.get_json()
        id = int(max(FICHAS.keys())) + 1
        FICHAS[id] = ficha
        return FICHAS[id], 201