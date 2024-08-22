import os
import zipfile
import kaggle
from kaggle.api.kaggle_api_extended import KaggleApi
from cnnClassifier import logger
from cnnClassifier.utils.common import get_size
from cnnClassifier.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    
    def download_file(self) -> str:
        # Authenticate with Kaggle API
        api = KaggleApi()
        api.authenticate()
        logger.info(f"Kaggle API Authenticated")
        
        try: 
            dataset_url = f"{self.config.kaggle_dataset_owner}/{self.config.kaggle_dataset_name}"
            zip_download_dir = self.config.local_data_file
            os.makedirs("artifacts/data_ingestion", exist_ok=True)
            logger.info(f"Downloading data from {dataset_url} into file {zip_download_dir}")
            api.dataset_download_files(dataset_url, path=zip_download_dir, unzip=False)
            logger.info(f"Downloaded dataset from kaggle to {zip_download_dir}")
            #logger.info(f"Downloaded dataset from kaggle to {self.config.root_dir}")
        
        except Exception as e:
            raise e
      
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        zip_file_path = os.path.join(self.config.local_data_file, 'chest-ctscan-images.zip')
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)  

        
        logger.info(f"Extracted dataset to {unzip_path}")