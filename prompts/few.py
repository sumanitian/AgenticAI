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

Rule:
- Strictly follow the output in JSON format

Output Format:
{{
 "code": "string" or None,
 "isCodingQuestion": boolean
}}

Examples:
Q: Can you explain the a + b whole square?
A: {{"code": null, "isCodingQuestion": false}}

Q: Hey, Write a code in python for adding two numbers.
A: {{"code": def add(a, b):
        return a + b, "isCodingQuestion": false}}

"""

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {
            "role": "user",
            "content": "Hey, write a code to add n number in js"
        }
    ]
)

print(response.choices[0].message.content)
