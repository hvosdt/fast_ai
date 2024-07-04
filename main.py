from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
import os
import json
from passport import recognize
from calls import recognize_call
import requests

app = FastAPI()

UPLOAD_DIR = 'uploads'
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post('/upload/{lead_id}')
async def upload_file(lead_id: int, file: UploadFile = File(...)):
    #if authorization != 'Bearer Asdf2121':
    #    return HTTPException(status_code=401, detail='Unauthorized')
    
    file_path = os.path.join(UPLOAD_DIR, f'{lead_id}_{file.filename}')
    with open(file_path, 'wb') as f:
        contents = await file.read()
        f.write(contents)
    result = recognize(file_path)
    print(result)
    
    return {'status': 'success', 'payload': result}

class Call(BaseModel):
    link: str
    call_id: str
    
@app.post('/out_call/{link}')
async def out_call(link):
    response = requests.get(link)
    
    filename = f'123.ogg' 
    with open(filename, 'wb') as f:
        f.write(response.content)
                
    result = recognize_call(filename)
    print(result)
    
    return {'status': 'success', 'payload': result}
