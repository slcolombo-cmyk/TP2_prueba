from flask import Flask
from dotenv import load_dotenv
from flask_restful import Api

import main.resources as resources

#Inicializar restful
api = Api()

# Inicializar la aplicacion Flask
def create_app():

    #Inicializar la aplicacion Flask
    app = Flask(__name__)

    #cargamos las variables de entorno
    load_dotenv()

    #cargar los recursos
    api.add_resource(resources.PacienteResource, '/paciente/<id>')
    api.add_resource(resources.PacientesResource, '/pacientes')

    api.init_app(app)

    return app

