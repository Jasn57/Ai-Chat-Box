import openai
from config import API_KEY

openai.api_key = API_KEY

def ask_gpt(history):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=history
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"[Error] {str(e)}"
