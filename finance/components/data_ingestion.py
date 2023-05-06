from finance.logger import logging
from finance.exception import FinanceException
from finance.entity.config_entity import DataIngestionConfig
from finance.entity.artifact_entity import DataIngestionArtifact, StockSelection


import os,sys,json
import urllib.request
import pandas as pd



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
            stock = StockSelection.stock_selected
            download_url =f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={stock}.BSE&outputsize=full&apikey={api_key}"


            #target download dir

            target_download_dir = self.data_ingestion_config.feature_store_file_path

            os.makedirs(target_download_dir,exist_ok=True)

            target_file_path = os.path.join(target_download_dir,stock)
            print(target_file_path)

            # Download the stock data

            logging.info(f"Downloading data from {download_url} to {target_download_dir}. ")
            
            urllib.request.urlretrieve(download_url,target_file_path)
            logging.info("Data downloaded sucessfully.")

        except Exception as e:
            raise FinanceException(e, sys)
    def transform_into_data_frame(self):
        try:
            #Fetchinf the data dir
            data_dir = self.data_ingestion_config.feature_store_file_path
            stock_selected = StockSelection.stock_selected

            data_file_path = os.path.join(data_dir,stock_selected)
            print(data_file_path)

            # read the JSON file
            with open(data_file_path, 'r') as f:
                 data = json.load(f)

            # extract the column data from the JSON file
            columns = list(data['Time Series (Daily)']['2023-02-24'].keys())

            # create an empty data frame with the extracted column names
            df = pd.DataFrame(columns=columns)

            # iterate over the JSON data and add rows to the data frame
            for date, values in data['Time Series (Daily)'].items():
                row = [float(values[column]) for column in columns]
                df.loc[date] = row

            print(df)

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
            self.transform_into_data_frame()
            # self.export_data_into_feature_store()
        except Exception as e:
            raise FinanceException(e, sys)
