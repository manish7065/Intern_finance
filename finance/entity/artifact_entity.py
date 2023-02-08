from dataclasses import dataclass


@dataclass
class DataIngestionArtifact:

    trained_file_path:str  #path to save train data
    test_file_path:str     #path to save testing data


