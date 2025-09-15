from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

client = OpenAI(
    api_key = api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": "consider youself as only maths expert, if you get any question other than maths then say, sorry i will answer maths question"},
        {
            "role": "user",
            "content": "Hey, Can you help me solve the a + b whole square"
        }
    ]
)

print(response.choices[0].message.content)


# response = client.chat.completions.create(
#     model = "gemini-2.5-flash",
#     message=[
#         {"role": "user", "content": "Hey There"}
#     ]
# )