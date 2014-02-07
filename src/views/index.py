import webapp2
import settings
    
class IndexPage(webapp2.RequestHandler):
    "Stub request handler"

    def get(self):
        template_values = dict()
        template = settings.JINJA_ENVIRONMENT.get_template(
            'index/index.html')
        self.response.write(template.render(template_values))


class SaibaMaisPage(webapp2.RequestHandler):

    def get(self):
        template_values = dict()
        template = settings.JINJA_ENVIRONMENT.get_template(
            'index/saiba_mais.html')
        self.response.write(template.render(template_values))

