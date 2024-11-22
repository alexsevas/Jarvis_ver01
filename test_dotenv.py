import os
import dotenv

dotenv.load_dotenv()
GROQ_API = os.getenv('GROQ_API')
GENAI_API = os.getenv('GENAI_API')

print (f'GROQ_API - {GROQ_API}')
print (f'GENAI_API - {GENAI_API}')