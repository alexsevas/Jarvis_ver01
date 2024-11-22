# conda activate jarvis2
# чат с llama3-70b-8192 через API groq

import os
import dotenv
from groq import Groq

dotenv.load_dotenv()
GROQ_API = os.getenv('GROQ_API')
groq_client = Groq(api_key=GROQ_API)

def  groq_prompt(prompt):
    convo = [{'role': "user", 'content': prompt}]
    chat_completion = groq_client.chat.completions.create(messages=convo, model='llama3-70b-8192')
    response = chat_completion.choices[0].message

    return response.content

prompt = input('USER: ')
response = groq_prompt(prompt)
print(response)