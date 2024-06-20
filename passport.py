import google.generativeai as genai
import os
import pathlib
import json
import config
import re

genai.configure(api_key=config.GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-1.5-flash')

def clean_json_string(json_string):
    pattern = r'^```json\s*(.*?)\s*```$'
    cleaned_string = re.sub(pattern, r'\1', json_string, flags=re.DOTALL)
    return cleaned_string.strip()

def recognize(filename):
    cookie_picture = {
        'mime_type': 'image/png',
        'data': pathlib.Path(f'{filename}').read_bytes()
    }

    prompt = "Распознай заграничный паспорт и верни данные с такими полями: Номер документа, Имя, Фамилия, Отчество, Гражданство, Дата рождения, Дата выдачи, Дата окончания срока, Пол, Место рождения. Если в поле есть спецсимволы или слова на латинице, то их объеденить. В полях могут быть данные, отделенные символом слеш."

    response = model.generate_content(
        contents=[prompt, cookie_picture]
    )
    j = json.loads(clean_json_string(response.text))
    
    res = {
        'number': j['Номер документа'],
        'name': j['Имя'],
        'surname': j['Фамилия'],
        'parentname': j['Отчество'],
        'bdate': j['Дата рождения'],
        'expire_date': j['Дата окончания срока'],
        'issue_date': j['Дата выдачи'],
        'citizenship': j['Гражданство'],
        'place_of_birth': j['Место рождения'],
        'gender': j['Пол'],        
        }
    return res