import os,sys
from src.abalone.logger import logging
from src.abalone.exception import CustomException
from dotenv import load_dotenv
import pymysql
import pandas as pd

load_dotenv()

host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
db = os.getenv('db')


def read_sql_data():
    logging.info("Reading SQL database started")
    try:
        mydb = pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db
        )
        logging.info("Connection Established: %s", mydb)
        df = pd.read_sql_query('Select * from abalone', mydb)
        print(df.head())

        return df



    except Exception as ex:
        raise CustomException(ex)