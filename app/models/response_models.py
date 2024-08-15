from pydantic import BaseModel

# class ConversionResponse(BaseModel):
#     file_path: str
    
class ConversionResponse(BaseModel):
    message: str
    file_path: str
    url_link: str