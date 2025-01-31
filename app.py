from src.abalone.logger import logging
from src.abalone.exception import CustomException
import sys
from src.abalone.components.data_ingestion import DataIngestionConfig, DataIngestion

if __name__ == "__main__":
    logging.info("Test")

    try:
        # data_ingestion_config=DataIngestionConfig()
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion() #when run only ingestion.py


    except CustomException as e:
        logging.error(e)
        raise CustomException(e,sys)