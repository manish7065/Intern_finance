from finance.exception import FinanceException
from finance.logger import logging
from finance.entity.config_entity import TrainingPipelineConfig,DataIngestionConfig
from finance.entity.artifact_entity import DataIngestionArtifact
from finance.components.data_ingestion import DataIngestion

import os,sys


class TrainPipeline:
    is_pipeline_running = False
    def __init__(self):
        self.training_pipeline_config=TrainingPipelineConfig()

    def start_data_ingestion(self)-> DataIngestionArtifact:
        try:
            logging.info("starting data ingestion.")
            self.data_ingestion_config = DataIngestionConfig(
                training_pipeline_config = self.training_pipeline_config)
            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()


        except Exception as e:
            raise FinanceException(e, sys)


    def run_pipeline(self):
        try:
            TrainPipeline.is_pipeline_running = True
            data_ingestion_artifact:DataIngestionArtifact = self.start_data_ingestion()

        except Exception as e:
            TrainPipeline.is_pipeline_running = False
            raise FinanceException(e, sys)