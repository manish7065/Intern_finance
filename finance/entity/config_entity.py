from finance.constant import training_pipeline
from datetime import datetime
import os,sys


class TrainingPipelineConfig:
    """
    This class will provide the training pipeline configuration.
    Which contain:
        pipeline_name
        artifact_dir
        time_stamp
    """
    def __init__(self,timestamp=datetime.now()):
        timestamp = timestamp.strftime("%m_%d_%Y_%H_%M_%S")
        self.pipeline_name = training_pipeline.PIPELINE_NAME
        self.artifact_dir = os.path.join(training_pipeline.ARTIFACT_DIR,timestamp)
        self.time_stamp = timestamp
        # self.FILE_NAME = # have to give the stock_name.csv to store in feature store

# Data Ingestion Configuration 
class DataIngestionConfig:
    """
    This class contains the methods to perforn the various functionalities of the data ingestion. 
    """
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):

        self.data_ingestion_dir:str=os.path.join(
            training_pipeline_config.artifact_dir,training_pipeline.DATA_INGESTION_DIR_NAME
        )
        
        self.feature_store_file_path:str = os.path.join(
            self.data_ingestion_dir,training_pipeline.DATA_INGESTION_FEATURE_STORE_DIR
        )

    