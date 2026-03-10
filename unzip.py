import zipfile

zip_file_path = "../data/health-care-data-set-20-tables.zip"
extract_to = "../data"

with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extract_to)

print("Dataset extracted successfully into the data folder.")
