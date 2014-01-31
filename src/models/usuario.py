from endpoints_proto_datastore.ndb import EndpointsModel
from google.appengine.ext import ndb

class Aparelho(EndpointsModel):
    nome = ndb.StringProperty(indexed=True)
    token = ndb.StringProperty(indexed=True)
    last_sampling = ndb.DateProperty()

    @classmethod
    def validate_login(cls, name, token):
        aparelhos = cls.query(cls.token == token).iter()
        for aparelho in aparelhos:
        	if aparelho.nome == name:
        		return aparelho
        return None