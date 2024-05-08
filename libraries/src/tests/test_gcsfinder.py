import unittest
from unittest.mock import MagicMock
from gcsfinder import GCSAPI

class TestGCSAPI(unittest.TestCase):
    def setUp(self):
        self.logger = MagicMock()
        self.gcs_api = GCSAPI(self.logger)

    def test_bucket_existence(self):
        self.gcs_api.client.get_bucket = MagicMock(return_value=True)

        result = self.gcs_api.check_bucket_existence("gambaro_bucket")

        self.assertTrue(result)
        self.logger.info.assert_called_once_with("Il bucket 'gambaro_bucket' esiste.")

    def test_bucket_non_existence(self):
        self.gcs_api.client.get_bucket = MagicMock(side_effect=Exception("Bucket not found"))

        result = self.gcs_api.check_bucket_existence("gambaro_bucke")

        self.assertFalse(result)
        self.logger.error.assert_called_once_with(
            "Il bucket 'gambaro_bucke' non esiste. Errore: Bucket not found")

    def test_upload_file_to_bucket_success(self):
        bucket_mock = MagicMock()
        blob_mock = MagicMock()
        self.gcs_api.client.get_bucket = MagicMock(return_value=bucket_mock)
        bucket_mock.blob = MagicMock(return_value=blob_mock)

        bucket_name = "gambaro_bucket"
        file_path = "libraries/src/src/src/test.txt"
        destination_blob_name = "test_blob.txt"

        self.gcs_api.upload_file_to_bucket(bucket_name, file_path, destination_blob_name)

        self.gcs_api.client.get_bucket.assert_called_once_with(bucket_name)
        bucket_mock.blob.assert_called_once_with(destination_blob_name)
        blob_mock.upload_from_filename.assert_called_once_with(file_path)
        self.logger.info.assert_called_once_with(
            f"File caricato con successo nel bucket '{bucket_name}': {destination_blob_name}"
        )

    def test_upload_file_to_bucket_failure(self):
        self.gcs_api.client.get_bucket = MagicMock(side_effect=Exception("Test error"))

        bucket_name = "gambaro_bucket"
        file_path = "libraries/src/src/src/test.txt"
        destination_blob_name = "test_blob.txt"

        self.gcs_api.upload_file_to_bucket(bucket_name, file_path, destination_blob_name)

        # Assertions
        self.gcs_api.client.get_bucket.assert_called_once_with(bucket_name)
        self.logger.error.assert_called_once_with(
            f"Errore durante il caricamento del file nel bucket '{bucket_name}': Test error"
        )

if __name__ == '__main__':
    unittest.main()
