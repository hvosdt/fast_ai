from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import FileResponse, JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
import os
import json
from passport import recognize
#from calls import recognize_call
import requests


from dp import recognize_url, recognize_local
from openai_client import get_recommendations

app = FastAPI()

from aws_textract import recognize_passport

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
    result = recognize_passport(file_path)
    print(result)
    
    return {'status': 'success', 'payload': result}

class Call(BaseModel):
    link: str
    call_id: str
    
@app.get('/out_call')
async def out_call(call: Call):    
    ext = call.link.split('.')[-1]
    filename = '{call_id}.{ext}'.format(call_id = call.call_id,
                                        ext = ext)
    response = requests.get(call.link)
    
    with open(filename, 'wb') as file:
        file.write(response.content)
    
    call_text = recognize_local(filename)
    call_recomendations = get_recommendations(call_text)
    
    result = {
        'text': call_text,
        'recomendations': call_recomendations
    }
    
    return JSONResponse(content=jsonable_encoder(result))
