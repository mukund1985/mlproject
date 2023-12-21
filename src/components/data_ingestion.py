import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass, field
from src.exception import CustomException
from src.logger import logging

@dataclass
class DataIngestionConfig:
    """
    Configuration class for data ingestion, with default file paths and parameters for data split.
    """
    train_data_path: str = field(default_factory=lambda: os.path.join('artifacts', "train.csv"))
    test_data_path: str = field(default_factory=lambda: os.path.join('artifacts', "test.csv"))
    raw_data_path: str = field(default_factory=lambda: os.path.join('artifacts', "data.csv"))
    input_data_path: str = field(default_factory=lambda: 'notebook/data/stud.csv')
    test_size: float = 0.2
    random_state: int = 42

class DataIngestion:
    def __init__(self):
        """
        Constructor for the DataIngestion class, initializing the configuration.
        """
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        """
        Main method for data ingestion process.
        """
        logging.info("Entered the data ingestion method or component")
        try:
            # Validate input file path
            if not os.path.exists(self.ingestion_config.input_data_path):
                raise FileNotFoundError(f"Input file not found: {self.ingestion_config.input_data_path}")

            # Reading the dataset into a DataFrame
            df = pd.read_csv(self.ingestion_config.input_data_path)
            logging.info(f'Read the dataset as dataframe with {df.shape[0]} rows and {df.shape[1]} columns')

            # Create directory for saving the files if it doesn't exist
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            # Save the raw data to the specified path in CSV format
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            logging.info(f"Saved raw data to {self.ingestion_config.raw_data_path}")

            # Splitting the dataset into training and testing sets
            train_set, test_set = train_test_split(df, test_size=self.ingestion_config.test_size, random_state=self.ingestion_config.random_state)
            logging.info("Train test split completed")

            # Save the training and testing set to their respective paths
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            logging.info(f"Training and testing data saved to {self.ingestion_config.train_data_path} and {self.ingestion_config.test_data_path}")

            return self.ingestion_config.train_data_path, self.ingestion_config.test_data_path
        except Exception as e:
            logging.error(f"Error during data ingestion: {str(e)}")
            raise CustomException(e, sys)
        
if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()
