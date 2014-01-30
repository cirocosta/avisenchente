# Gets the data from the IoT-sdk-python and transforms it 
# to Datastore objects so that we are able to put on the database.

import iotsdk

from datetime import datetime
from models import measures


class Fetcher(object):
    """Gets the data from the webservice and puts into the Datastore"""

    def __init__(self, token):
        self.token = token
        self.iot = iotsdk.Iot(self.token)

    def _convertToDatetime(self, str_time):
        try:
            time = datetime.strptime(str_time, "%Y-%m-%dT%H:%M:%SZ")
            return time
        except:
            return None

    def _toDatabaseMeasure(self, dict_measure):
        has_something = 0
        measure = None
        if dict_measure:
            measure = measures.Measure()
            try:
                str_time = dict_measure['st']
                measure.sampling_time=self._convertToDatetime(str_time)
                has_something = 1
            except:
                pass
            try:
                dict_measure['ms']
                ms = dict_measure['ms']
                measure.name = ms['p']
                measure.value = ms['v']
                measure.unit = ms['u']
                has_something = 1
            except:
                pass
            try:
                dict_measure['pms']
                #saber do que se trata pms
            except:
                pass

        return measure if has_something else None

    def _toDatabaseMeasureCollection(self, dict_measure_collection):
        measures = []
        try:
            data = dict_measure_collection['data']
            for ms in data:
                try:
                    measure = self._toDatabaseMeasure(ms)
                    if measure:
                        measures.append(measure)
                except:
                    # a bad dict
                    pass
        except:
            # dict without the data element
            pass
        return measures

    def fetch_data(self,**kwargs):
        return self.iot.get_device_data(**kwargs)

