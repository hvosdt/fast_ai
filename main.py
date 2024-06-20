from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import FileResponse
import os
from passport import recognize

app = FastAPI()

UPLOAD_DIR = 'uploads'
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post('/upload/{lead_id}')
async def upload_file(lead_id: int, file: UploadFile = File(...), authorization: str=None):
    if authorization != 'Bearer Asdf2121':
        return HTTPException(status_code=401, detail='Unauthorized')
    
    file_path = os.path.join(UPLOAD_DIR, f'{lead_id}_{file.filename}')
    with open(file_path, 'wb') as f:
        contents = await file.read()
        f.write(contents)
    result = recognize(file_path)
    print(result)
        
    return {'starus': 'success', 'message': result}
