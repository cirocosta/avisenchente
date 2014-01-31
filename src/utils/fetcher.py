# Gets the data from the IoT-sdk-python and transforms it 
# to Datastore objects so that we are able to put on the database.

import iotsdk

from datetime import datetime
from models import measures
from models import usuario


class Fetcher(object):
    """Gets the data from the webservice and puts into the Datastore"""

    def __init__(self, token):
        self.token = token
        self.iot = iotsdk.Iot(self.token)

    def _convertToDatetime(self, str_time):
        """ Converts the date from string to a datetime Object"""
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
        """ Transforma um objeto que contem uma lista de dicionarios
        puros representantes de medidas de aparelho em uma lista
        de objetos de medicao compativeis com a Database """
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

    def _getAparelho(self):
        """ Verifica no iterator do cursor se ha um elemento.
        Se este houver, retorna o mesmo (no caso de multiplos com o 
        mesmo token retornaria apenas o primeiro) """
        aparelhos = usuario.Aparelho().\
            query(usuario.Aparelho.token == self.token).iter()
        if aparelhos.has_next():
            return aparelhos.next()
        return None

    def _getTillLast(self, limit, aparelho, last):
        """ Obtenho o primeiro offset para um limite.
            Itero sobre os elements obtidos ate
            haver um break. Retorna entao a lista inteira
            com tudo """
        i = 0
        result = []
        while True:
            data_collection = self.iot.get_device_data(limit=limit, 
                sortBy="!samplingTime", offset=limit*i)
            db_measure_collection = self._toDatabaseMeasureCollection(\
                data_collection)
            for measure in db_measure_collection:
                result.append(measure)
                if measure.sampling_time == last:
                    break
        return result

    def update_database_data(self):
        """ Fetches all of the data that is related to the
        device that corresponds to the given token """
        data = self.iot.get_device_data(limit=10, sortBy="!samplingTime")
        measure_collection = self._toDatabaseMeasureCollection(data)
        for measure in measure_collection:
            measure.put()
