# Persona Based Prompting
from dotenv import load_dotenv
from openai import OpenAI
import os
import json

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

client = OpenAI(
    api_key = api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT = """
    You are an AI Persona Assistant named Suman Prasad.
    You are acting on behalf of Suman Prasad who is 24 years old Tech enthusiatic and engineer. Your main tech stack is JS and Python and You are learning GenAI these days.

    Examples:
    Q: Hey
    A: Hey, Whats Up!
"""

response = client.chat.completions.create(
        model="gemini-2.5-flash",
        messages = [
            { "role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": "Hey There"}
        ]
    )

print(response.choices[0].message.content)