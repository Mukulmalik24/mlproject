import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

             # decorator - inside the class, to define a class variable we use __init__.
           # by using this @dataclass, we will be able to define the variable without __init__
           # if we only have to define some variable inside the class, better gor with @dataclass
           # if we have to write the functions and define variables, go with __init__
@dataclass
class DataIngestionConfig:
    train_data_path : str = os.path.join('artifacts','train.csv') #train.csv will be saved inside artifacts folder
    test_data_path : str = os.path.join('artifacts','test.csv')
    raw_data_path : str = os.path.join('artifacts','data.csv')


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig() # all thedata paths defined above get read here
    
    def initiate_data_ingestion(self):
        logging.info("Enetered the data ingestion method or component")
        try: # for any error popping up
            df=pd.read_csv('notebook\data\stud.csv') #instead wecan read from any other source like mysql, mongoDb etc
            logging.info('Read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header =True)

            logging.info("Train_test_split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False,header=True) #saved the train set in csv
            train_set.to_csv(self.ingestion_config.test_data_path, index=False,header=True) #saved the test set in csv

            logging.info("Ingestion of the data is completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path, #next modeule - data transformation will take these dataset andstart the process

            )
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__ == '__main__':
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()
    
    data_transformation = DataTransformation()
    data_transformation.initiate_data_transformation(train_data, test_data)
        