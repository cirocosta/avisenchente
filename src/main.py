import webapp2
import settings

from views import index
from views import pedido
from views import usuario
from views import fetcher
from views import regiao
from views import paypal


application = webapp2.WSGIApplication([
    ('/', index.IndexPage),
    ('/saiba_mais', index.SaibaMaisPage,),
    
    ('/adquirir', pedido.SamplePedido,),
    ('/adquirir/carrinho', pedido.AdquirirCarrinho,),
    ('/adquirir/carrinho/detalhes', pedido.CarrinhoDetalhes,),
    ('/adquirir/carrinho/finalizar', pedido.CarrinhoFinalizar,),
    
    ('/paypal/setexpresscheckout', paypal.PayPalSEC,),
    ('/paypal/getexpresscheckoutdetails', paypal.PayPalGECD,),
    ('/paypal/ipn', paypal.PayPalIPN,),

    ('/usuario/token/([a-zA-Z0-9]+)', usuario.UsuarioIndex,),
    ('/usuario/criar', usuario.AparelhoCriar,),
    ('/usuario/login', usuario.Login,),
    ('/usuario/data/([a-zA-Z]+)/([a-zA-Z0-9]+)', usuario.UsuarioData,),

    ('/fetch_data', fetcher.FetcherCron,),
    ('/regiao/([a-zA-Z]+)', regiao.RegiaoIndex,),
], debug=settings.DEBUG)
