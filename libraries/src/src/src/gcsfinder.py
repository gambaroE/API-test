from google.cloud import storage
from logger import Logger


class GCSAPI:
    def __init__(self, logger):
        self.logger = logger
        self.client = storage.Client()

    def check_bucket_existence(self, bucket_name):
        try:
            self.client.get_bucket(bucket_name)  # Controlla se il bucket esiste
            self.logger.info(f"Il bucket '{bucket_name}' esiste.")
            return True
        except Exception as e:
            self.logger.error(f"Il bucket '{bucket_name}' non esiste. Errore: {e}")
            return False

    def download_file_from_bucket(self, bucket_name, file_path):
        blob = self.client.bucket(bucket_name).blob(file_path)
        blob.download_to_filename(file_path)
        self.logger.info(f"File scaricato con successo: {blob.name}")

    def upload_file_to_bucket(self, bucket_name, file_path, destination_blob_name):
        try:
            blob = self.client.get_bucket(bucket_name).blob(destination_blob_name)
            blob.upload_from_filename(file_path)
            self.logger.info(f"File caricato con successo nel bucket '{bucket_name}': {destination_blob_name}")
        except Exception as e:
            self.logger.error(f"Errore durante il caricamento del file nel bucket '{bucket_name}': {e}")
