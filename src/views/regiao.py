import webapp2
import settings

class RegiaoIndex(webapp2.RequestHandler):

    def get(self, nome_regiao):
        template_values = dict()
        template = settings.JINJA_ENVIRONMENT.get_template(
            'regiao/index.html')
        self.response.write(template.render(template_values))