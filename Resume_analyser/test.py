import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# Get only model names
models = [model.name for model in genai.list_models()]
for model in models:
    print(model)