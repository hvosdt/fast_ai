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

def get_okk_dialog(text):
    client = OpenAI(project='proj_N4qPODMfw3cTgDsgKdeF3fcR', api_key=config.OPENAI_SECRET_KEY)

    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {   
                "role": "system", 
                "content": 
                    '''Ты аналитик отдела контроля качества. Дай развернутую и не шаблонную аналитику по диалогу с клиентом, который был в переписки и по телефону.
                    В результате нужна общая оценка в баллах.
                    Анализ нужно провести по следующим параметрам:
                    1. Название параметра: Приветсвтвие.  Как оценивать: Менеджер поприветствовал клмента. Оценка в балах: 0 или 1
                    2. Название параметра: Назвал свое имя.  Как оценивать: Менеджер назвал свое имя. Оценкав балах: 0 или 1
                    3. Название параметра: Самопрезентация.  Как оценивать: Менеджер сказал название компании. Оценка в балах: 0 или 1
                    4. Название параметра: Апелляция.  Как оценивать: Менеджер уточнил, оставлял ли клиент заявку. Оценка в бадах: 0 или 1'''},
            {
                "role": "user", "content": text}
        ]
        )

    return completion.choices[0].message.content
