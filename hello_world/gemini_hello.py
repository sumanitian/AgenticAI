from dotenv import load_dotenv
from google import genai
import os

load_dotenv() 

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(
    api_key = api_key,
)

response = client.models.generate_content(
  model='gemini-2.5-flash',
  contents='Explain how AI works in a few words',
)

print(response.text)

# from google import genai
# import time

# client = genai.Client(
#     api_key = "AIzaSyDgutt4h5TxndzzInRMBLw383UmAdruQkI"
# )

# while True:
#     try:
#         response = client.models.generate_content(
#             model='gemini-2.5-flash',
#             contents="Explain how AI works in a few words",
#         )
#         print(response.text)
#         break  # Exit the loop if the request is successful
#     except genai.errors.ServerError as e:
#         print(f"Server error: {e}. Retrying in 5 seconds...")
#         time.sleep(5)  # Wait for 5 seconds before retrying
# print(response.text)