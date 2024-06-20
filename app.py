from fastapi import FastApi, File, UploadFile, HTTPExeption
from fastapi.response import FileResponse
import os

app = FastApi()

UPLOAD_DIR = 'uploads'
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post('/upload/{id}')
async def upload_file(lead_id: int, file: UploadFile = File(...), authorization: str=None):
    if authorization != 'Bearer Asdf2121':
        return HTTPexception(status_code=401, detail='Unauthorized')
    
    file_path = os.path.join(UPLOAD_DIR, f'{lead_id}_{file.filename}')
    with open(file_path, 'wb') as f:
        contents = await file.read()
        f.write(contents)
    return {'starus': 'success', 'message': 'File uploaded successfully'}
