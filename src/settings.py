import jinja2
import os

DEBUG = True
JINJA_ENVIRONMENT = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.join(os.getcwd() + '/templates')),
    extensions = ['jinja2.ext.autoescape'],
    autoescape = True,)

# PayPal
PP_MODE = "sandbox"
PP_TESTACCOUNT = "ciro.costa-facilitator@usp.br"
PP_SANDBOX_ENDPOINT = "api.sandbox.paypal.com"
PP_CLIENT_ID = "Ad4GARBAggxw3gWtJ2Hp7jb8fL4njBwzcyPaIMiBLdpwsVBLcvDyOR5lJBkR"
PP_SECRET = "EOCx4RAfEaYAGtLE28BOml0zwYdk-rvt6_01coHI7Cf44rwaE_DM73_mj9js"
