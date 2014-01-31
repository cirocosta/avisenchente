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
