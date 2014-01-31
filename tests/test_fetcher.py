import unittest
import samples

from src.utils import iotsdk
from src.utils import fetcher


class TestFetcher(unittest.TestCase):
    """ Tests src.utils.fetcher """

    def setUp(self):
        self.fetcher = fetcher.Fetcher("dummy_token")
        pass

    def test_initialization(self):
        self.assertEqual(self.fetcher.token, "dummy_token")
        self.assertIsInstance(self.fetcher.iot, iotsdk.Iot)


    def test_toDatabaseMeasure(self):
        self.assertFalse(self.fetcher._toDatabaseMeasure(dict()))
        self.assertFalse(self.fetcher._toDatabaseMeasure(\
            samples.SAMPLE_FALSE_MEASURE))
        self.assertTrue(self.fetcher._toDatabaseMeasure(\
            samples.SAMPLE_TRUE_MEASURE))

    def test_toDatabaseMeasureCollection(self):
        self.assertFalse(self.fetcher._toDatabaseMeasureCollection(\
            samples.SAMPLE_FALSE_MEASURE_COLLECTION))
        self.assertTrue(self.fetcher._toDatabaseMeasureCollection(\
            samples.SAMPLE_TRUE_MEASURE_COLLECTION))

    def test_fetch_data(self):
        pass


if __name__ == "__main__":
    unittest.main()


    