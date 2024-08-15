import pytest
from app.core.config import INPUT_DIR
from app.services.converter import convert_mp4_to_wav
from pathlib import Path



def test_convert_mp4_to_wav():
    input_file = "sample1.mp4"
    input_file= Path(INPUT_DIR) / Path(input_file)
    output_file , output_file_path = convert_mp4_to_wav(input_file , "en", "test")
    
    assert Path(output_file).exists()
    assert output_file.endswith(".wav")

# from io import BytesIO
# from pathlib import Path
# from fastapi.testclient import TestClient
# from app.main import app

# client = TestClient(app)

# def test_convert_file():
#     input_file = "sample2.mp4"
#     input_file= Path(INPUT_DIR) / Path(input_file)
#     with open(input_file, "rb") as file:
#         response = client.post("/convert", files={"file": ("sample2.mp4", file, "video/mp4")})
    
#     assert response.status_code == 200
#     assert "file_path" in response.json()
