from pathlib import Path
from fastapi.testclient import TestClient
from app.core.config import INPUT_DIR
from app.main import app

client = TestClient(app)

def test_convert_file():
    input_file = "sample.mp4"
    input_file= Path(INPUT_DIR) / Path(input_file)
    print("ldgskgvonsd", input_file)
    with open(input_file, "rb") as file:
        response = client.post("/convert", files={"file": file}, data={"language": "English"} )
    
    assert response.status_code == 200
    assert "file_path" in response.json()

# from fastapi.testclient import TestClient
# from app.main import app
# from io import BytesIO

# client = TestClient(app)

# def test_convert_file():
#     input_file = "sample2.mp4"
#     input_file= Path(INPUT_DIR) / Path(input_file)
    
#     # Read the file content
#     with open(input_file, "rb") as file:
#         file_content = file.read()
    
#     # Send the file as a byte stream with the correct filename and MIME type
#     response = client.post("/convert", files={"file": ("sample2.mp4", BytesIO(file_content), "video/mp4")})
    
#     assert response.status_code == 200
#     assert "file_path" in response.json()
