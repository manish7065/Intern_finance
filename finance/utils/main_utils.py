from finance.logger import logging
from finance.exception import FinanceException

import os,sys
import yaml

def read_yaml_file(file_path:str) -> dict:
    try:
        with open(file_path,'r') as file:
            return yaml.safe_load(file)
            
    except Exception as e:
        raise FinanceException(e, sys)