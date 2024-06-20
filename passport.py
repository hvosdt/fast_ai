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

    prompt = "Распознай заграничный паспорт и верни данные с такими полями: номер документа, Имя, Фамилия, Отчество, Гражданство, Дата рождения, Дата выдачи, Дата окончания срока, Пол, Место рождения."

    response = model.generate_content(
        contents=[prompt, cookie_picture]
    )
    
    #return response.to_dict()
    #return result['candidates'][0]['content']['parts'][0]['text']
    return clean_json_string(response.text)