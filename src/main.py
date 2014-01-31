import webapp2
import settings

from views import index
from views import pedido
from views import usuario
from views import fetcher

application = webapp2.WSGIApplication([
    ('/', index.IndexPage),
    ('/pedido', pedido.SamplePedido,),
    ('/usuario/token/([a-zA-Z0-9]+)', usuario.UsuarioIndex,),
    ('/usuario/criar', usuario.AparelhoCriar,),
    ('/usuario/login', usuario.Login,),
    ('/fetch_data', fetcher.FetcherCron,),
    ('/usuario/data/([a-zA-Z]+)/([a-zA-Z0-9]+)', usuario.UsuarioData,),	
], debug=settings.DEBUG)
