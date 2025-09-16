# zero Shot Prompting
# The model is given a direct question or task without prior examples.

from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

client = OpenAI(
    api_key = api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT = "You should only and only answer the coding releated questions. Do not answer anything else. Your name is Alexa. If user asks something other than coding, just say sorry."

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {
            "role": "user",
            "content": "Hey, Can you write a python code to translate the hello to hindi"
        }
    ]
)

print(response.choices[0].message.content)
