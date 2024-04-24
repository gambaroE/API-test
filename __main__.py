from bqfinder import BigQueryAPI
from gcsfinder import GCSAPI
import logging


class Logger:
    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def info(self, message):
        self.logger.info(message)

    def error(self, message):
        self.logger.error(message)


def main():
    logger = Logger()
    bq_api = BigQueryAPI(logger)
    gcs_api = GCSAPI(logger)

    logger.info("Benvenuto!")
    scelta = input(
        "Quale operazione vuoi eseguire?\n1. Verifica esistenza tabella BigQuery\n2. Verifica esistenza bucket GCS\nScelta (1/2):")

    if scelta == "1":
        table_path = input("Inserisci il nome della tabella (progetto.dataset.nome):\n")
        bq_api.check_table_existence(table_path)
    elif scelta == "2":
        bucket_name = input("Inserisci il nome del bucket GCS:\n")
        if gcs_api.check_bucket_existence(bucket_name):
            choice = input("Il bucket esiste. Vuoi scaricare/caricare un file?\n(caricare(1)/scaricare(2)):\n ")
            if choice.lower() == "caricare" or choice.lower() == "1":
                file_path = input("Inserisci il percorso del file da caricare:\n")
                destination_blob_name = input("Inserisci path di destinazione nel bucket:\n")
                gcs_api.upload_file_to_bucket(bucket_name, file_path, destination_blob_name)
            elif choice.lower() == "scaricare" or choice.lower() == "2":
                bucket_file = input("Inserisci il nome del file nel bucket GCS: ")
                gcs_api.download_file_from_bucket(bucket_name, bucket_file)
            else:
                logger.info("Operazione terminata.")
        else:
            logger.error(f"Il bucket '{bucket_name}' non esiste.")
    else:
        logger.error("Scelta non valida.")


if __name__ == "__main__":
    main()
