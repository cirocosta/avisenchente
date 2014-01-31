import webapp2
import settings
import time
import json

from datetime import datetime
from models import usuario
from models import measures
from utils import fetcher

SENSOR_TYPES = {
    "luminosidade": "luminousIntensity",
    "ruido": "sound",
    "temperatura": "temperature",
    "humidade": "relativeHumidity"
}

def _datetimeToUnixTime(dt_date):
    return time.mktime(dt_date.timetuple())


class UsuarioIndex(webapp2.RequestHandler):
    """ Index page for the user
    IT LACKS A SESSION. REALLY NON-SECURE BY NOW.
    """

    def get(self, token):
        aparelho = usuario.Aparelho().get_aparelho_from_token(token)
        template_values = {
            "token": aparelho.token if aparelho else None,
            "nome": aparelho.nome if aparelho else None
        }
        template = settings.JINJA_ENVIRONMENT.get_template(
            'usuario/index.html')
        self.response.write(template.render(template_values))

class UsuarioData(webapp2.RequestHandler):

    def get(self, sensor, token):

        mms = measures.Measure().\
            get_filtered_measures(SENSOR_TYPES[sensor], token)
        valores = [[measure.value, _datetimeToUnixTime(measure.sampling_time)] 
            for measure in mms]

        objeto = {
            "key": SENSOR_TYPES[sensor],
            "values": valores
        }

        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(json.dumps(objeto))


# class UsuarioRuido(webapp2.RequestHandler):

#     def get(self, token):
#         measures.Measure().get_filtered_measures("sound")


#         self.response.headers['Content-Type'] = 'application/json'
#         self.response.write(json.dumps(objeto))


# class UsuarioTemperatura(webapp2.RequestHandler):

#     def get(self, token):
#         measures.Measure().get_filtered_measures("temperature")

#         self.response.headers['Content-Type'] = 'application/json'
#         self.response.write(json.dumps(objeto))


# class UsuarioHumidade(webapp2.RequestHandler):

#     def get(self, token):
#         measures.Measure().get_filtered_measures("relativeHumidity")

#         self.response.headers['Content-Type'] = 'application/json'
#         self.response.write(json.dumps(objeto))


class Login(webapp2.RequestHandler):
    
    def get(self):
        template_values = dict()
        template = settings.JINJA_ENVIRONMENT.get_template(
            'usuario/login.html')
        self.response.write(template.render(template_values))

    def post(self):
        nome = self.request.get('nome')
        token = self.request.get('token')
        if usuario.Aparelho().validate_login(nome, token):
            self.response.write(json.dumps({"success":True}))
        else:
            self.response.write(json.dumps({"success":False}))


class AparelhoCriar(webapp2.RequestHandler):
    """ Handler para a criacao de usuario """

    def get(self):
        template_values = dict()
        template = settings.JINJA_ENVIRONMENT.get_template(
            'usuario/criar.html')
        self.response.write(template.render(template_values))

    def post(self):
        nome = self.request.get("nome")
        token = self.request.get("token")
        if nome and token:
            aparelho = usuario.Aparelho(nome=nome, token=token)
            aparelho.put()
            self.response.write(json.dumps({"success": True}))
        else:
            self.response.write(json.dumps({"success": False}))

