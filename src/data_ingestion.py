import os
import sys
import pandas as pd

from src.logging import get_logger
from src.exception import CustomException

logging = get_logger(__name__)


class DataIngestion:
    def __init__(self, data_path="notebook/data/Datasets.csv", save_dir="artifacts"):
        """
        Data Ingestion Config
        """
        self.data_path = data_path
        self.save_dir = save_dir
        self.raw_data_path = os.path.join(save_dir,'Dataset.csv')
        # create the directory if it doesn't exist

        os.makedirs(save_dir,exist_ok=True)

    def initiate_data_ingestion(self):
        """
        Data Ingestion Process
        """
        try:
            logging.info("Initiating Data Ingestion Process")
            df = pd.read_csv(self.data_path)

            logging.info("Loading and Cleaning the Dataset")
            #Drop Columns
            df_drop = ["Unnamed: 0","nameOrig", "nameDest"]
            df = df.drop(columns=df_drop,errors="ignore")

            # Handling Missing Values
            logging.info("Handling Missing Values")
            df = df.dropna()

            # Saving Cleaned Dataset
            logging.info("Cleaned Dataset Saved")
            df.to_csv(self.raw_data_path, index=False)

            return self.raw_data_path
        except Exception as e:
            raise CustomException(e,sys)


if __name__ == "__main__":
    ingestion = DataIngestion(data_path="notebook/data/datasets.csv")
    processed_data_path = ingestion.initiate_data_ingestion()