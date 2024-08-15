import os
from dotenv import load_dotenv
from pathlib import Path

# Load .env file
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# Configuration variables
UPLOAD_DIR = os.getenv("UPLOAD_DIR", "./uploads")
OUTPUT_DIR = os.getenv("OUTPUT_DIR", None)
INPUT_DIR = os.getenv("INPUT_DIR", "./samples")
LOG_DIR = os.getenv("LOG_DIR", "./app")
DEBUG = os.getenv("DEBUG", "False") == "True"
HOST = os.getenv("HOST", "127.0.0.1")
PORT = int(os.getenv("PORT", 8000))
ALLOWED_FILE_TYPES = os.getenv("ALLOWED_FILE_TYPES", "video/mp4").split(",")
MAX_UPLOAD_SIZE = os.getenv("MAX_UPLOAD_SIZE", "50MB")
