# from app.core.config import HOST, PORT

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run("app.main:app", host=HOST, port=PORT, reload=True)

import os
import sys
from importlib.metadata import PackageNotFoundError
import os
import sys

from flask import jsonify
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.utils.file_utils import get_complete_new_file_name, log_download
from app.utils.file_utils import get_complete_new_file_name

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pathlib import Path
from app.core.config import*
# from ..core.config import HOST, PORT # type: ignore
from app.core.config import HOST, PORT
from fastapi import FastAPI
from app.api.routes import router
app = FastAPI()

# Mount the static directory
app.mount("/static", StaticFiles(directory="app/static"), name="static")
def check_packages():
    packages_to_check = ["langchain==0.0.0", "llama_index==0.9.11", "flask==2.3.2", "flask_cors==3.0.10","pandas"]
    results = {}

    for package in packages_to_check:
        package_name, _, desired_version = package.partition("==")

        try:
            installed_version = version(package_name)
            if installed_version == desired_version:
                results[package] = "installed"
            else:
                results[package] = f"installed, but version {installed_version} instead of {desired_version}"
        except PackageNotFoundError:
            results[package] = "not installed"

    return results

@app.route('/check_packages', methods=['GET'])
def route_check_packages():
    results = check_packages()
    return jsonify(results)
@app.get("/", response_class=HTMLResponse)
async def read_index():
    index_file_path = Path("app/static/index.html")
    return index_file_path.read_text()


# Include the router with the endpoint
app.include_router(router)
@app.get("/")
async def root():
    return {"message": "MP4 to WAV Converter API"}
@app.route("/hola")
def hello_world():
    return "Hello World!"




if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host=HOST, port=PORT, reload=True)

   
