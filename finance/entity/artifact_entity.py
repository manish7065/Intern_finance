from dataclass import dataclass


@dataclass
class UserSelection:
    stock_name:str

@dataclass
class DataIngestionArtifact:

    trained_file_path:str  #path to save train data
    test_file_path:str     #path to save testing data


@dataclass
pass