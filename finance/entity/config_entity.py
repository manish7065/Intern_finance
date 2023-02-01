from finance.constant import training_pipeline
from datetime import datetime
import os,sys


class TrainingPipelineConfig:
    def __init__(self,timestamp=datetime.now()):
        timestamp = timestamp.strftime("%m_%d_%Y_%H_%M_%S")
        self.pipeline_name = training_pipeline.PIPELINE_NAME
        self.artifact_dir = os.path.join(training_pipeline.ARTIFACT_DIR,timestamp)
        self.time_stamp = timestamp

# Data Ingestion Config
class DataIngestionConfig:
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        self.data_ingestio
