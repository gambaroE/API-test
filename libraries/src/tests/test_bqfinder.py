import unittest
from unittest.mock import MagicMock
from bqfinder import BigQueryAPI


class TestBigQueryAPI(unittest.TestCase):
    def setUp(self):
        self.logger = MagicMock()
        self.bigquery_api = BigQueryAPI(self.logger)

    def test_table_existence(self):
        self.bigquery_api.client.get_table = MagicMock(return_value=True)
        result = self.bigquery_api.check_table_existence("training-gcp-309207.Gambaro_api.test_api")

        self.assertTrue(result)
        self.logger.info.assert_called_once_with("La tabella 'test_api' esiste in 'training-gcp-309207.Gambaro_api'.")

    def test_table_non_existence(self):
        self.bigquery_api.client.get_table = MagicMock(side_effect=Exception("Table not found"))
        result = self.bigquery_api.check_table_existence("training-gcp-309207.Gambaro_api.test_ap")
        self.assertFalse(result)
        self.logger.error.assert_called_once_with(
            "La tabella 'test_ap' non esiste nel percorso 'training-gcp-309207.Gambaro_api'. Errore: Table not found")


if __name__ == '__main__':
    unittest.main()
