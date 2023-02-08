import os,sys


"""
Training Pipeline related constants
"""
PIPELINE_NAME = 'finance'
ARTIFACT_DIR = 'artifact'
# FILE_NAME = #will have to keep dynamic or in yaml file

TRAIN_FILE_NAME = ''
TEST_FILE_NAME = ''

PROCESSING_OBJECT_FILE_NAME = ""
MODEL_FILE_NAME = ""
SCHEMA_FILE_PATH = ""



"""
Data Ingestion related constant start with DATA_INGESTION
"""

DATA_INGESTION_COLLECTION_NAME = ''
DATA_INGESTION_DIR_NAME = 'data_ingestion'
DATA_INGESTION_FEATURE_STORE_DIR = 'feature_store'
DATA_INGESTION_DATA_STORE_DIR = 'data_store'
DATA_INGESTION_DATA_SPLIT_DIR = 'split_store'
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO : float = 0.2

"""
Data Validation related constants start with DATA_VALIDATION
"""

