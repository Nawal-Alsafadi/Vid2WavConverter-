import os
import subprocess
from pathlib import Path

from fastapi import HTTPException
from app.core.config import OUTPUT_DIR
import tempfile

from app.utils.file_utils import get_complete_new_file_name, get_downloads_folder

# def convert_mp4_to_wav(input_file: str) -> str:
#     output_file = Path(OUTPUT_DIR) / Path(input_file).with_suffix(".wav").name
#     command = ['ffmpeg', '-i', input_file, str(output_file)]
    
#     subprocess.run(command, check=True)
    
#     return str(output_file)
def convert_mp4_to_wav(input_file: str , language : str , base_name : str) -> str:
    try:
        print("Hola " , language )
        print("Hola  base_name " , base_name  )
        
        d = get_downloads_folder()

        print("input_file ", input_file)
        # Create a temporary file for the output WAV
        # output_file_path = Path(d) / Path(input_file).with_suffix(".wav").name
        output_file_path = get_complete_new_file_name(base_name, "(Audio)")
        print("##########################################################33 output_file_path ya my eyes ", output_file_path)

        temp_output_file = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
        output_file = temp_output_file.name

        # Run the conversion command
        command = ['ffmpeg', '-i', input_file, output_file_path]
        subprocess.run(command, check=True)
        print("output_file hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh" , output_file)
        print("output_file hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh -> " , output_file_path)
        
        return output_file , output_file_path
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to convert file: {str(e)}")
    finally:
        # Clean up the input file after conversion
        if Path(input_file).exists():
            Path(input_file).unlink()


########################
import io
import ffmpeg

def convert_mp4_to_wav_bytes(input_file: io.BytesIO) -> io.BytesIO:
    # Create an in-memory bytes buffer for the output
    print(" in func ", input_file)
    output_buffer = io.BytesIO()
    print(" in func 2 ", output_buffer)

    # Run the ffmpeg process
    process = (
        ffmpeg
        .input('pipe:0')  # Read from the input stream
        .output('pipe:1', format='wav')  # Write to the output stream as WAV
        .run_async(pipe_stdin=True, pipe_stdout=True, pipe_stderr=True)
    )
    
    # Write the input file to ffmpeg's stdin
    output, error = process.communicate(input=input_file.read())

    if process.returncode != 0:
        raise Exception(f"ffmpeg error: {error.decode()}")

    # Write the output to the output buffer
    output_buffer.write(output)
    output_buffer.seek(0)  # Rewind the buffer to the beginning

    return output_buffer
#############################################
import tempfile

def convert_mp4_to_wav1(input_file: bytes) -> str:
    with tempfile.NamedTemporaryFile(suffix=".mp4", delete=False) as temp_input_file:
        temp_input_file.write(input_file)
        temp_input_file.flush()  # Ensure the file is written
        temp_input_path = temp_input_file.name

    output_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
    output_file_path = output_file.name
    output_file.close()  # Close the file to ensure ffmpeg can write to it

    command = ['ffmpeg', '-i', temp_input_path, output_file_path]
    subprocess.run(command, check=True)
    print("output_file_path : ", output_file_path)

    return output_file_path