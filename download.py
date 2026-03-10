from kaggle.api.kaggle_api_extended import KaggleApi
import os

#api authentication
api = KaggleApi()
api.authenticate()

dataset_name = "moid1234/health-care-data-set-20-tables"

# Change this to any path you want
download_path = "home/vicky/project/raw_data"

# Create folder if it doesn't exist
os.makedirs(download_path, exist_ok=True)

print(f"Downloading dataset {dataset_name} to {download_path} ...")
api.dataset_download_files(dataset_name, path=download_path, unzip=False)
print("Download complete!")
