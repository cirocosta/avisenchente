import webapp2
import settings

from views import index
from views import pedido
from views import usuario
from views import fetcher
from views import regiao

application = webapp2.WSGIApplication([
    ('/', index.IndexPage),
    ('/saiba_mais', index.SaibaMaisPage,),
    ('/adquirir', pedido.SamplePedido,),
    ('/adquirir/carrinho', pedido.AdquirirCarrinho,),
    ('/adquirir/carrinho/detalhes', pedido.CarrinhoDetalhes,),
    ('/usuario/token/([a-zA-Z0-9]+)', usuario.UsuarioIndex,),
    ('/usuario/criar', usuario.AparelhoCriar,),
    ('/usuario/login', usuario.Login,),
    ('/fetch_data', fetcher.FetcherCron,),
    ('/usuario/data/([a-zA-Z]+)/([a-zA-Z0-9]+)', usuario.UsuarioData,),	
    ('/regiao/([a-zA-Z]+)', regiao.RegiaoIndex,),
], debug=settings.DEBUG)
