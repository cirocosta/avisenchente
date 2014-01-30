import webapp2
import settings

from views import index
from views import pedido

application = webapp2.WSGIApplication([
    ('/', index.IndexPage),
    ('/pedido', pedido.SamplePedido,),
], debug=settings.DEBUG)
