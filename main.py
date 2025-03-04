from fastapi import FastAPI, BackgroundTasks
import subprocess
import os
from pathlib import Path

app = FastAPI()
DOWNLOAD_DIR = "downloads"

os.makedirs(DOWNLOAD_DIR, exist_ok=True)

def download_song(url: str):
    subprocess.run(["spotdl", url, "--output", f"{DOWNLOAD_DIR}/"], check=True)

@app.post("/download/")
async def download_music(url: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(download_song, url)
    return {"message": "Descarga en progreso"}

@app.get("/files/")
def list_downloads():
    files = os.listdir(DOWNLOAD_DIR)
    return {"files": files}

@app.get("/files/{filename}")
def get_file(filename: str):
    file_path = Path(DOWNLOAD_DIR) / filename
    if file_path.exists():
        return {"url": f"/{DOWNLOAD_DIR}/{filename}"}
    return {"error": "Archivo no encontrado"}
