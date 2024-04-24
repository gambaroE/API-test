import unittest
from unittest.mock import MagicMock
from bqfinder import BigQueryAPI


class TestBigQueryAPI(unittest.TestCase):
    def setUp(self):
        self.logger = MagicMock()
        self.bigquery_api = BigQueryAPI(self.logger)

    def test_table_existence(self):
        # Mock get_table method to return a truthy value
        self.bigquery_api.client.get_table = MagicMock(return_value=True)

        # Call the method with a valid table path
        result = self.bigquery_api.check_table_existence("training-gcp-309207.Gambaro_api.test_api")

        # Assertions
        self.assertTrue(result)
        self.logger.info.assert_called_once_with("La tabella 'test_api' esiste in 'training-gcp-309207.Gambaro_api'.")

    def test_table_non_existence(self):
        # Mock get_table method to raise an exception
        self.bigquery_api.client.get_table = MagicMock(side_effect=Exception("Table not found"))

        # Call the method with a non-existent table path
        result = self.bigquery_api.check_table_existence("training-gcp-309207.Gambaro_api.test_ap")

        # Assertions
        self.assertFalse(result)
        self.logger.error.assert_called_once_with(
            "La tabella 'test_ap' non esiste nel percorso 'training-gcp-309207.Gambaro_api'. Errore: Table not found")


if __name__ == '__main__':
    unittest.main()
