from fastapi import APIRouter, UploadFile, File, HTTPException, status , Form
from app.services.converter import convert_mp4_to_wav
from app.models.response_models import ConversionResponse
from app.utils.file_utils import log_download, save_upload_file
from app.core.config import ALLOWED_FILE_TYPES

router = APIRouter()

# @router.post("/convert", response_model=ConversionResponse)
# async def convert_file(file: UploadFile = File(...)):
#     if file.content_type not in ALLOWED_FILE_TYPES:
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST, 
#             detail=f"Invalid file type: {file.content_type}. Allowed types: {ALLOWED_FILE_TYPES}"
#         )
    
#     saved_file_path = save_upload_file(file)
#     output_file_path = convert_mp4_to_wav(saved_file_path)
    
#     return ConversionResponse(file_path=output_file_path)
@router.get("/hola", response_model=ConversionResponse)
async def convert_file():
 
    
    # Return the path to the converted file
    return ConversionResponse(message="File has been successfully converted and saved.",
        file_path="output_file_path")

@router.post("/convert", response_model=ConversionResponse)
async def convert_file(file: UploadFile = File(...) , language: str = Form(...)):
    if file.content_type not in ALLOWED_FILE_TYPES:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=f"Invalid file type: {file.content_type}. Allowed types: {ALLOWED_FILE_TYPES}"
        )

    # Save the uploaded file to a temporary file
    saved_file_path , base_name = save_upload_file(file)
    print("Debug 0 " , type(base_name))
    # Convert the file
    output_file ,output_file_path = convert_mp4_to_wav(saved_file_path , language , base_name)
    print("Debug 1 " , output_file_path)
    print("Debug 1 " , type(output_file_path))
    # Log the download
    log_download(str(output_file_path))
    
    print(f"Download notification: {output_file_path} has been converted and logged.")
        # Create the download URL
    download_url = f"{output_file_path}"
    
    # Return the path to the converted file
    return ConversionResponse(message="File has been successfully converted and saved.",
        file_path=str(output_file_path), url_link = download_url)

@router.post("/convert1", response_model=ConversionResponse)
async def convert_file(file: UploadFile = File(...), language: str = Form(...)):
    if file.content_type not in ALLOWED_FILE_TYPES:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid file type: {file.content_type}. Allowed types: {ALLOWED_FILE_TYPES}"
        )

    # Save the uploaded file to a temporary file
    saved_file_path, base_name = save_upload_file(file)

    # Convert the file
    output_file_path = convert_mp4_to_wav(saved_file_path, language, base_name)

    # Log the download
    log_download(output_file_path)

    # Create the download URL
    download_url = f"/downloads/{base_name}.wav"

    # Return the response with a message, file path, and download URL
    return ConversionResponse(
        message="File has been successfully converted and saved.",
        file_path=output_file_path,
        download_url=download_url
    )




# from fastapi import FastAPI, File, UploadFile
# from app.services.converter import convert_mp4_to_wav


# @router.post("/convert")
# async def convert_file(file: UploadFile = File(...)):
#     contents = await file.read()
#     output_path = convert_mp4_to_wav(contents)
#     return {"file_path": output_path}
