import os
import shutil
import kagglehub

def ensure_dataset(destination_folder="data"):
    """
    Checks if dataset exists in `data/`. If not, downloads from KaggleHub.
    Returns the full path to OnlineRetail.csv
    """
    dest_file = os.path.join(destination_folder, "OnlineRetail.csv")

    if os.path.exists(dest_file):
        print(f"Dataset already exists at: {dest_file}")
        return dest_file

    print("Dataset not found. Downloading from Kaggle...")
    # KaggleHub download
    download_path = kagglehub.dataset_download("vijayuv/onlineretail")
    csv_file = os.path.join(download_path, "OnlineRetail.csv")
    if not os.path.exists(csv_file):
        raise FileNotFoundError(f"CSV not found in KaggleHub download folder: {csv_file}")

    # Ensure data folder exists
    os.makedirs(destination_folder, exist_ok=True)

    # Copy CSV to data folder
    shutil.copy(csv_file, dest_file)
    print(f"CSV copied to: {dest_file}")
    return dest_file
