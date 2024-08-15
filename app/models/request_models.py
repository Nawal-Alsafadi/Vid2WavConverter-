# Example for additional request data if needed
from pydantic import BaseModel

class FileUploadRequest(BaseModel):
    additional_data: str
    language:str
