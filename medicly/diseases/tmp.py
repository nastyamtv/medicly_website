import openai
import json

openai.api_key = "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"  # Використовуй свій OpenAI API ключ

user_message = "Hello"
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": user_message}]
)
print(response)