import endpoints

from google.appengine.ext import ndb
from endpoints_proto_datastore.ndb import EndpointsModel


class Measure(EndpointsModel):
    """Stores all the measures of that are gotten from the IoT-kit"""
    
    name = ndb.StringProperty(indexed=True)
    unit = ndb.StringProperty(indexed=False)
    value = ndb.FloatProperty()
    sampling_time = ndb.DateProperty()
    inserted_at = ndb.DateProperty(auto_now_add=True)

    @classmethod
    def get_filtered_measures(cls, m_filter, token):
    	""" Retorna as medidas do aparelho de um usuario que e 
    		identificado por seu token """
    	return cls.query(cls.name == m_filter, cls.token == token).iter()

