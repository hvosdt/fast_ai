import google.generativeai as genai
import os
import pathlib
import json
import config
import re
import prompts

genai.configure(api_key=config.GOOGLE_API_KEY)
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "application/json",
}
prompt = "Распознай файл. Это разговор менеджера по продажам с клиентом. Дай оценку с точки зрения менеджера, что и как можно улучшить в этом разговоре, текст разговора тоже верни. Ответ на русском языке."

def clean_json_string(json_string):
    pattern = r'^```json\s*(.*?)\s*```$'
    cleaned_string = re.sub(pattern, r'\1', json_string, flags=re.DOTALL)
    return cleaned_string.strip()

def recognize_call(filename):
    model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    # safety_settings = Adjust safety settings
    # See https://ai.google.dev/gemini-api/docs/safety-settings
    )

    cookie_picture = {
        'mime_type': 'audio/ogg',
        'data': pathlib.Path(f'{filename}').read_bytes()
    }    

    response = model.generate_content(
        contents=[prompts.calls, cookie_picture]
    )
    print(response.text)
    j = json.loads(clean_json_string(response.text))        
    return j

if __name__ == '__main__':
    r = recognize_call('call.ogg')
    print(r)