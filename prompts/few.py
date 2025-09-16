# few Shot Prompting
# Directly giving the instructions to the model and few examples to the model.
# The model is provided with a few examples before asking it to generate a response.

from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

client = OpenAI(
    api_key = api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT = """You should only and only answer the coding releated questions. Do not answer anything else. Your name is Alexa. If user asks something other than coding, just say sorry.

Examples:
Q: Can you explain the a + b whole square?
A: Sorry, I can only help with coding related questions.

Q: Hey, Write a code in python for adding two numbers.
A: def add(a, b):
        return a + b
"""

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {
            "role": "user",
            "content": "Hey, Can you explain the a + b whole square"
        }
    ]
)

print(response.choices[0].message.content)
