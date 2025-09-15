from dotenv import load_env
from openai import OpenAI

load_env()

client = OpenAI()

response = client.chat.completions.create(
    model = "gpt-4o-mini",
    message=[
        {"role": "user", "content": "Hey There"}
    ]
)

print(response.choices[0].message.content)