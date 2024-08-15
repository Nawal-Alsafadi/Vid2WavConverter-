# from pathlib import Path
# import pytest
# from app.core.config import INPUT_DIR
# from app.services.converter import convert_mp4_to_wav
# from io import BytesIO

# def test_convert_mp4_to_wav():
#     # Use a BytesIO object to simulate a file
#     input_file = "te.mp4"
#     input_file= Path(INPUT_DIR) / Path(input_file)
    
#     with open(input_file, "rb") as f:
#         input_file = BytesIO(f.read())
    
#     output_file = convert_mp4_to_wav(input_file.getvalue())

#     assert Path(output_file).exists()
#     assert output_file.endswith(".wav")
