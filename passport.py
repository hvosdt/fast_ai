import google.generativeai as genai
import os
import pathlib
import json
import config
import re

genai.configure(api_key=config.GOOGLE_API_KEY)
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "application/json",
}
prompt = "Распознай заграничный паспорт и верни данные с такими полями: Номер документа, Имя, Фамилия, Отчество, Гражданство, Дата рождения, Дата выдачи, Дата окончания срока, Пол, Место рождения. Данные в полях разделены на кирилицу и латиницу. Верни данные на латинице"

def clean_json_string(json_string):
    pattern = r'^```json\s*(.*?)\s*```$'
    cleaned_string = re.sub(pattern, r'\1', json_string, flags=re.DOTALL)
    return cleaned_string.strip()

def recognize(filename):
    model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    # safety_settings = Adjust safety settings
    # See https://ai.google.dev/gemini-api/docs/safety-settings
    )

    cookie_picture = {
        'mime_type': 'image/png',
        'data': pathlib.Path(f'{filename}').read_bytes()
    }    

    response = model.generate_content(
        contents=[prompt, cookie_picture]
    )
    print(response.text)
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

if __name__ == '__main__':
    r = recognize('21688211_photo_2024-06-21_18.04.57.jpeg')
    print(r)