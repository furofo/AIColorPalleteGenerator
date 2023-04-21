# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import openai
from dotenv import dotenv_values
config = dotenv_values(".env")
openai.api_key = config["apiKey"]
prompt = """
You are a color palette generating assistant that responds to text prompts for color palettes.
Desired Format: A JSON array of hexadecimal color codes.
Text: a beautiful sunset
"""
response = openai.Completion.create(
    model="text-davinci-003",
    prompt = prompt,
    max_tokens=200,
)
print(response)
print(response["choices"][0]["text"])
