from finance.logger import logging
from finance.exception import FinanceException
from finance.entity.config_entity import DataIngestionConfig
from finance.entity.artifact_entity import DataIngestionArtifact


import os,sys
import urllib.request



class DataIngestion:
    def __init__(self,data_ingestion_config:DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config
            # self._schema_config = 
        except Exception as e:
            raise FinanceException(e, sys)

    def download_stock_data(self):
        try:
            # Creating the download url
            api_key = '6YKJO21SVQDCYFHF' # will set it in environment
            stock="TATAMOTORS"  #will have to varry as per the user selection
            download_url =f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={stock}.BSE&outputsize=full&apikey={api_key}"


            #target download dir

            target_download_dir = self.data_ingestion_config.feature_store_file_path

            os.makedirs(target_download_dir,exist_ok=True)

            target_file_path = os.path.join(target_download_dir,stock)

            # Download the stock data

            logging.info(f"Downloading data from {download_url} to {target_download_dir}. ")
            
            urllib.request.urlretrieve(download_url,target_file_path)
            logging.info("Data downloaded sucessfully.")

        except Exception as e:
            raise FinanceException(e, sys)

    def split_data_as_train_test(self):
        try:
            pass
        except Exception as e:
            raise FinanceException(e, sys)
    def export_data_into_feature_store(self):
        """
        Export the API collected data to mongoDB.
        """
        try:
            self
        except Exception as e:
            raise FinanceException(e, sys)

    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        try:
            logging.info(f"{'<<'*10}Data ingestion Starts{'>>'*10}")
            self.download_stock_data()
            # self.export_data_into_feature_store()
        except Exception as e:
            raise FinanceException(e, sys)