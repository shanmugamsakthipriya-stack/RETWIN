import logging
import azure.functions as func
from etl import run_etl

def main(mytimer: func.TimerRequest) -> None:
    logging.info("Azure Function ETL triggered.")
    try:
        run_etl()
        logging.info("ETL run completed successfully.")
    except Exception as e:
        logging.error(f"ETL run failed: {e}")
