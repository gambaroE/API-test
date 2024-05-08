import unittest
from unittest.mock import patch, MagicMock
from bqfinder import BigQueryAPI
from gcsfinder import GCSAPI
import logging
from __main__ import main

class Logger:
    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def info(self, message):
        self.logger.info(message)

    def error(self, message):
        self.logger.error(message)
class TestMainFunctionality(unittest.TestCase):
    @patch('builtins.input', side_effect=["1", "training-gcp-309207.Gambaro_api.test_api"])
    def test_check_table_existence(self, mock_input):
        logger = Logger()
        bq_api = BigQueryAPI(logger)

        logger.info = MagicMock()
        logger.error = MagicMock()

        main()

        bq_api.check_table_existence.assert_called_once_with("training-gcp-309207.Gambaro_api.test_api")
        logger.info.assert_any_call("Benvenuto!")

    @patch('builtins.input', side_effect=["2", "gambaro_bucket", "si", "ComandiGcloud.txt"])
    def test_check_bucket_existence_and_download(self, mock_input):
        logger = Logger()
        gcs_api = GCSAPI(logger)

        logger.info = MagicMock()
        logger.error = MagicMock()

        gcs_api.check_bucket_existence = MagicMock(return_value=True)

        gcs_api.download_file_from_bucket = MagicMock()

        main()

        gcs_api.check_bucket_existence.assert_called_once_with("gambaro_bucket")
        gcs_api.download_file_from_bucket.assert_called_once_with("gambaro_bucket", "ComandiGcloud.txt")
        logger.info.assert_any_call("Il bucket 'gambaro_bucket' esiste.")
        logger.info.assert_any_call("File scaricato con successo: file.txt")
        logger.info.assert_any_call("Operazione terminata.")

    @patch('builtins.input', side_effect=["3"])  # Invalid choice
    def test_invalid_choice(self, mock_input):
        logger = Logger()

        logger.info = MagicMock()
        logger.error = MagicMock()

        main()

        logger.error.assert_called_once_with("Scelta non valida.")

if __name__ == "__main__":
    unittest.main()
