import json
import os
import shutil
from pathlib import Path
import tempfile

from fastapi import HTTPException
from app.core.config import LOG_DIR, OUTPUT_DIR, UPLOAD_DIR
from datetime import datetime

import random

def save_upload_file1(upload_file):
    upload_dir = Path(UPLOAD_DIR)
    upload_dir.mkdir(parents=True, exist_ok=True)
    file_path = upload_dir / upload_file.filename
    
    with file_path.open("wb") as buffer:
        shutil.copyfileobj(upload_file.file, buffer)
    return str(file_path)

def save_upload_file(upload_file):
    try:
        base_name = os.path.splitext(upload_file.filename)[0]
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
        with temp_file as buffer:
            shutil.copyfileobj(upload_file.file, buffer)
        return temp_file.name , base_name 
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to save upload file: {str(e)}")
    
def get_downloads_folder():
    """Return the path to the Downloads folder."""
    if os.name == 'nt':  # For Windows
        path = Path(os.getenv('USERPROFILE')) / 'Downloads'
        print("os.name))))))))))))))))))))))))))))))))))))))))))))))))))) " , os.name )
    else:  # For macOS and Linux
        path = Path.home() / 'Downloads'
    
    return path

def generate_unique_filename(base_name, extension):
    """Generate a unique filename using the current timestamp and a random number."""
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    random_suffix = random.randint(1000, 9999)  # Adding a random number to reduce collision risk
    return f"{base_name}_{timestamp}_{random_suffix}{extension}"

def get_complete_new_file_name(base_name, extension):
    print("jjjj : ", OUTPUT_DIR)
    if OUTPUT_DIR and OUTPUT_DIR.strip(): 
        print("Not None ya my eyes" ,OUTPUT_DIR )
        downloades_folder = OUTPUT_DIR
    else:
        print(" None ya my eyes")
        downloades_folder = get_downloads_folder()
    print("final : ", downloades_folder)
    unique_filename = generate_unique_filename(base_name, extension)
    print("kashfksdbj  :  ", unique_filename)
    output_file_path = Path(downloades_folder) / Path(unique_filename).with_suffix(".wav").name
    return output_file_path 

# Function to log the download
from pathlib import Path
from datetime import datetime
import json

# Function to log the download
def log_download(file_path: str):
    # Determine the directory of the current script
    project_dir = Path(__file__).resolve().parent  # Resolves to the directory containing this script
    
    # Specify the log file path relative to the project directory
    log_file_path = project_dir / 'download_history.json'

    download_entry = {
        'file_path': file_path,
        'timestamp': datetime.now().isoformat()
    }
    
    try:
        # Open the log file and append the new entry
        with log_file_path.open('r+') as log_file:
            history = json.load(log_file)
            history.append(download_entry)
            log_file.seek(0)
            json.dump(history, log_file, indent=4)
    except FileNotFoundError:
        # If the file does not exist, create it and write the first entry
        with log_file_path.open('w') as log_file:
            json.dump([download_entry], log_file, indent=4)

