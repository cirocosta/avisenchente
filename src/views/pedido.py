import webapp2
import settings
    
class SamplePedido(webapp2.RequestHandler):
    "Stub request handler"

    def get(self):
        template_values = dict()
        template = settings.JINJA_ENVIRONMENT.get_template(
            'pedido/pedidos.html')
        self.response.write(template.render(template_values))


class AdquirirCarrinho(webapp2.RequestHandler):

    def get(self):
        template_values = dict()
        template = settings.JINJA_ENVIRONMENT.get_template(
            'pedido/carrinho.html')
        self.response.write(template.render(template_values))

class CarrinhoDetalhes(webapp2.RequestHandler):

    def get(self):
        template_values = dict()
        template = settings.JINJA_ENVIRONMENT.get_template(
            'pedido/carrinho_detalhes.html')
        self.response.write(template.render(template_values))
