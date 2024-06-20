import google.generativeai as genai
import os
import pathlib
import json
import config

genai.configure(api_key=config.GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-1.5-flash')

def recognize(filename):
    cookie_picture = {
        'mime_type': 'image/png',
        'data': pathlib.Path(f'{filename}').read_bytes()
    }

    prompt = "Распознай заграничный паспорт и верни данные в словаря с такими полями: номер документа, Имя, Фамилия, Отчество, Гражданство, Дата рождения, Дата выдачи, Дата окончания срока, Пол, Место рождения."

    response = model.generate_content(
        contents=[prompt, cookie_picture]
    )
    result = response.to_dict()
    
    #return response.to_dict()
    #return result['candidates'][0]['content']['parts'][0]['text']
    return response.text