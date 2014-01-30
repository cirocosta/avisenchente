import webapp2
import settings
    
class SamplePedido(webapp2.RequestHandler):
    "Stub request handler"

    def get(self):
        template_values = dict()
        template = settings.JINJA_ENVIRONMENT.get_template(
            'pedido/fechamento_pedido.html')
        self.response.write(template.render(template_values))
