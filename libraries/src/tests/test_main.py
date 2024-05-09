import unittest
from unittest.mock import MagicMock, patch
from io import StringIO
from main import main, Logger


class TestMain(unittest.TestCase):
    def setUp(self):
        self.logger = Logger()

    def test_check_table_existence(self):
        # Mocking BigQueryAPI.check_table_existence method
        with unittest.mock.patch('main.BigQueryAPI.check_table_existence') as mock_check_table_existence:
            mock_check_table_existence.return_value = True
            user_input = "1\ntraining-gcp-309207.Gambaro_api.test_api\n"
            with unittest.mock.patch('builtins.input', side_effect=user_input.split()):
                main()
                mock_check_table_existence.assert_called_with('training-gcp-309207.Gambaro_api.test_api')

    def test_check_bucket_existence(self):
        # Mocking GCSAPI.check_bucket_existence method
        with unittest.mock.patch('main.GCSAPI.check_bucket_existence') as mock_check_bucket_existence:
            mock_check_bucket_existence.return_value = True
            user_input = "2\ngambaro_bucket\nscaricare\nComandiGcloud.txt\n"
            with unittest.mock.patch('builtins.input', side_effect=user_input.split()):
                main()
                mock_check_bucket_existence.assert_called_with('gambaro_bucket')

    @patch('main.Logger', autospec=True)
    def test_invalid_choice(self, mock_logger):
        # Test invalid choice
        user_input = "3\n"
        with unittest.mock.patch('builtins.input', side_effect=user_input.split()):
            main()
            actual_message = mock_logger.method_calls[1].args[0]
            self.assertEqual(actual_message, "Scelta non valida.")




if __name__ == '__main__':
    unittest.main()
