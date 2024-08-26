import os
import zipfile
import kaggle
import shutil
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
        os.makedirs(unzip_path, exist_ok=True)
        zip_file_path = os.path.join(self.config.local_data_file,'chest-ctscan-images.zip')
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)  


        # Delete unnecessary folders (test and valid)
        folders_to_delete = ['test', 'valid']
        for folder in folders_to_delete:
            extract_path = os.path.join(unzip_path, 'Data')
            folder_path = os.path.join(extract_path, folder)
            if os.path.exists(folder_path):
                shutil.rmtree(folder_path)
            else:
                print(f"Folder {folder} does not exist.")
                
        files_to_move_and_rename = [
            {'name': 'adenocarcinoma_left.lower.lobe_T2_N0_M0_Ib', 'new_name': 'adenocarcinoma'},
            {'name': 'normal', 'new_name': 'normal'}
        ]  # Update with your file names and new names

        # Loop through the files to move and rename
        for file in files_to_move_and_rename:
            # Get the path to the current file
            file_path = os.path.join(unzip_path, 'Data','train', file['name'])
            
            # Check if the file exists
            if os.path.exists(file_path):
                # Move the file to the zip file path and rename it
                new_file_path = os.path.join(os.path.dirname(self.config.local_data_file), 'Data')
                shutil.move(file_path, new_file_path)
                
            else:
                print(f"File {file['name']} does not exist.")
        shutil.rmtree(os.path.join(unzip_path, 'Data','train')) # Remove the train folder

        
        logger.info(f"Extracted dataset to {unzip_path}")

