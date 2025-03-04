import os
import sys
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from imblearn.over_sampling import SMOTE

from src.logging import get_logger
from src.exception import CustomException

logging = get_logger(__name__)

class DataPreprocessing:
    def __init__(self, input_path ="artifacts/Dataset.csv", save_path="artifacts/preprocessed_data.csv"):
        """
        Data Preproceesing Stage
        Parameters:
        - input_path (str): Path to the cleaned Dataset.
        - save_path (str): Path to save the preprocessed Dataset.
        """
        self.input_path = input_path
        self.save_path = save_path

    def initialising_data_preprocess(self):
        try:
            logging.info("Loading the Cleaned Dataset")
            df = pd.read_csv(self.input_path)

            logging.info("Standardizing, Encoding and Transforming ")
            categorical_columns = ["type","branch","Acct type","Date of transaction","Time of day"]
            numerical_columns = [
                "step",
                "amount",
                "oldbalanceOrg",
                "newbalanceOrig",
                "unusuallogin"
                ]
            num_pipeline = Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="median")), ## Handling Missing Values
                    ("scaler",StandardScaler()) # Handling Standard Scaler
                ]
            )
            
            df[numerical_columns] = num_pipeline.fit_transform(df[numerical_columns])

            for col in categorical_columns:
                le = LabelEncoder()
                df[col] = le.fit_transform(df[col].astype(str))  # Convert to string before encoding

            logging.info('Handling Class Imbalance using SMOTE')
            X = df.drop(columns=["isFraud"])
            y = df["isFraud"]

            if y.value_counts()[0] > 2 * y.value_counts()[1]: 
                smote = SMOTE(sampling_strategy="auto", random_state=42)
                X_resampled, y_resampled = smote.fit_resample(X, y)
                df = pd.DataFrame(X_resampled, columns=X.columns)
                df["isFraud"] = y_resampled


            df.to_csv(self.save_path, index=False)
            logging.info('Data Preprocessing Completed')
            return self.save_path
        except Exception as e:
            raise CustomException(e,sys)
    
if __name__ == "__main__":
    preprocessing = DataPreprocessing()
    preprocessed_data = preprocessing.initialising_data_preprocess()