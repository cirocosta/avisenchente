import webapp2
import settings
import json

from models import usuario
from utils import fetcher


class UsuarioIndex(webapp2.RequestHandler):
    """ Index page for the user"""

    def get(self):
        template_values = dict()
        template = settings.JINJA_ENVIRONMENT.get_template(
            'usuario/index.html')
        self.response.write(template.render(template_values))

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

