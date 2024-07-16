import config
from openai import OpenAI

def get_recommendations(text):
    client = OpenAI(project='proj_N4qPODMfw3cTgDsgKdeF3fcR', api_key=config.OPENAI_SECRET_KEY)

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Ты аналитик отдела продаж. Дай рекомендации по этому диалогу с клиентом"},
            {"role": "user", "content": text}
        ]
        )

    return completion.choices[0].message['content']

