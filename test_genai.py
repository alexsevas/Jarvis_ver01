# conda activate jarvis2

import os
import dotenv
import google.generativeai as genai
import dotenv
from PIL import ImageGrab, Image

dotenv.load_dotenv()
GENAI_API = os.getenv('GENAI_API')
genai.configure(api_key=GENAI_API)

sys_msg = (
        'You are a multi-modal AI voice assistant. Your user may or may not have attached a photo for context '
        '(either a screenshot or a webcam capture). Any photo has already been processed into a highly detailed '
        'text prompt that will be attached to their transcribed voice prompt. Generate the most useful and '
        'factual response possible, carefully considering all previous generated text in your response before '
        'adding new tokens to the response. Do not expect or request images, just use the context if added. '
        'Use all of the context of this conversation so your response is relevant to the conversation. Make '
        'your responses clear and concise, avoiding any verbosity.'
    )

convo = [{'role': 'system', 'content': sys_msg}]

generation_config = {
    'temperature': 0.7,
    'top_p': 1,
    'top_k': 1,
    'max_output_tokens': 2048
}

safety_settings = [
    {
        'category': 'HARM_CATEGORY_HARASSMENT',
        'threshold': 'BLOCK_NONE'
    }
]
'''
model = genai.GenerativeModel('gemini-1.5-flash-latest',
                              generation_config=generation_config,
                              safety_settings=safety_settings
                              )
'''
model = genai.GenerativeModel('gemini-1.5-flash-latest')

img = Image.open('scree.jpg')
prompt = (
    'You are the vision analysis AI that provides semantic meaning from images to provide context '
    'to send to another AI that will create a response to the user. Do not respond as the AI assistant '
    'to the user. Instead take the user prompt input and try to extract all meaning from the photo '
    'relevant to the user prompt. Then generate as much objective data about the image for the AI '
    f'assistant who will respond to the user. Свой ответ сразу переводи на русский язык'
)
response = model.generate_content([prompt, img])
print(response.text)