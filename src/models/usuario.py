from endpoints_proto_datastore.ndb import EndpointsModel
from google.appengine.ext import ndb

class Aparelho(EndpointsModel):
    nome = ndb.StringProperty(indexed=True)
    token = ndb.StringProperty(indexed=True)
    last_sampling = ndb.DateProperty()

    @classmethod
    def validate_login(cls, name, token):
        """ Validacao super simples de login """
        aparelhos = cls.query(cls.token == token).iter()
        for aparelho in aparelhos:
        	if aparelho.nome == name:
        		return aparelho
        return None

    @classmethod
    def get_tokens(cls):
        """ Retorna uma lista de todos os tokens cadastrados """
        aparelhos = cls.query().iter()
        lista_tokens = []
        for aparelho in aparelhos:
            lista_tokens.append(aparelho.token)
        return lista_tokens

    @classmethod
    def get_aparelho_from_token(cls, token):
        """ Dado um token retorna o Aparelho se existir """
        aparelhos = cls.query(cls.token == token).iter()
        if aparelhos.has_next():
            return aparelhos.next()
        return None