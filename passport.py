import google.generativeai as genai
import os
import pathlib
import json
import config

genai.configure(config.GOOGLE_API_KEY)

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
    return response.to_dict()