from google.cloud import bigquery

class BigQueryAPI:
    def __init__(self, logger):
        self.logger = logger
        self.client = bigquery.Client()

    def check_table_existence(self, table_path):
        project_id, dataset_id, table_id = table_path.split('.')
        table_ref = f"{project_id}.{dataset_id}.{table_id}"

        try:
            self.client.get_table(table_ref)
            self.logger.info(f"La tabella '{table_id}' esiste in '{project_id}.{dataset_id}'.")
            return True
        except Exception as e:
            self.logger.error(
                f"La tabella '{table_id}' non esiste nel percorso '{project_id}.{dataset_id}'. Errore: {e}")
            return False
