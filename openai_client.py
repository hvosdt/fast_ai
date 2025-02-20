import config
from openai import OpenAI

def get_recommendations(text):
    client = OpenAI(project='proj_N4qPODMfw3cTgDsgKdeF3fcR', api_key=config.OPENAI_SECRET_KEY)

    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Ты аналитик отдела продаж. Дай развернутую и не шаблонную аналитику по диалогу с клиентом. А так же рекомендации по улучшению именно этого диалога."},
            {"role": "user", "content": text}
        ]
        )

    return completion.choices[0].message.content

def get_wazzap_recomendations(text):
    client = OpenAI(project='proj_N4qPODMfw3cTgDsgKdeF3fcR', api_key=config.OPENAI_SECRET_KEY)

    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Ты аналитик отдела продаж. Дай развернутую и не шаблонную аналитику по диалогу с клиентом. А так же рекомендации по улучшению именно этого диалога."},
            {"role": "user", "content": text}
        ]
        )

    return completion.choices[0].message.content

def get_lead_recomendations(text):
    client = OpenAI(project='proj_N4qPODMfw3cTgDsgKdeF3fcR', api_key=config.OPENAI_SECRET_KEY)

    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Ты аналитик отдела продаж. Дай развернутую и не шаблонную аналитику по диалогу с клиент, который был в переписки и по телефону. А так же рекомендации по улучшению именно этого диалога."},
            {"role": "user", "content": text}
        ]
        )

    return completion.choices[0].message.content
