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
    api.add_resource(resources.UsuarioResource, '/usuario/<id>')
    api.add_resource(resources.UsuariosResource, '/usuarios')
    api.add_resource(resources.FichasResource, '/fichas')
    api.add_resource(resources.FichaResource, '/ficha/<id>')
    api.add_resource(resources.PlanesResource, '/planes')
    api.add_resource(resources.PlanResource, '/plan/<id>')

    #api.add_resource(resources.NotificacionesResource, '/notificaciones')
    #api.add_resource(resources.LogoutResource, '/logout')
    #api.add_resource(resources.LoginResource, '/login')
    #api.add_resource(resources.RegisterResource, '/register')

    api.init_app(app)

    return app

