import webapp2
import settings

from views import index
from views import pedido
from views import usuario

application = webapp2.WSGIApplication([
    ('/', index.IndexPage),
    ('/pedido', pedido.SamplePedido,),
    ('/usuario', usuario.UsuarioIndex,),
    ('/usuario/criar', usuario.AparelhoCriar,),
    ('/usuario/login', usuario.Login,),
], debug=settings.DEBUG)
